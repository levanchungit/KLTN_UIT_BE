#!/usr/bin/env python3
"""
Comprehensive LLM Test Script for Transaction Classification
Tests with full metrics: F1 Score, Precision, Recall, Accuracy
Uses qwen2.5-7b model on llama.cpp server

Usage:
    python test_llm_7b_direct.py [--sample N] [--file FILE]
"""

import requests
import json
import sys
import time
import csv
import argparse
from collections import defaultdict
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

# ==================== CONFIGURATION ====================
DEFAULT_LLM_URL = 'http://127.0.0.1:8080/v1/chat/completions'
DEFAULT_MODEL = 'qwen2.5-7b-instruct-q4_k_m.gguf'
DEFAULT_TEST_FILE = 'data/evaluation/aligned_test_100.csv'
DEFAULT_OUTPUT_FILE = 'data/evaluation_results.txt'

# Categories from the actual dataset
DATASET_CATEGORIES = [
    'Ăn uống', 'Đi lại', 'Nhà ở', 'Mua sắm', 
    'Giải trí', 'Giáo dục', 'Y tế', 'Thu nhập', 'Chưa xác định'
]

# ==================== SYSTEM PROMPT ====================
CATEGORIES_STR = ', '.join(f'"{cat}"' for cat in DATASET_CATEGORIES)

SYSTEM_PROMPT = f'''BAN LA AI PHAN LOAI GIAO DICH TAI CHINH VIET NAM.

NHIEM VU:
- amount: So tien VND
- category: Danh muc giao dich (CHON 1 trong: {CATEGORIES_STR})
- type: Loai giao dich (Thu nhap/Chi phi)
- confidence: Do tin cay (0.0-1.0)

DANH MUC (BAT BUOC CHON 1):
{CATEGORIES_STR}

QUY TAC PHAN LOAI:
- An uong: An uong, thuc pham, cho, sieu thit, com, bun, pho, lau
- Di lai: Xang xe, taxi, bus, grab, xe om, ve xe, di chuyen, do xe, gui xe
- Nha o: Tien nha, dien nuoc, gas, wifi nha, phi quan ly, chung cu
- Mua sam: Quan ao, tui xach, giay dep, do dien tu, vat dung ca nhan
- Giai tri: Game, phim, du lich, giai tri, netflix, spotify, karaoke
- Giao duc: Hoc phi, sach vo, khoa hoc, dung cu hoc tap
- Y te: Thuoc, kham benh, benh vien, y te, sieu thit thuoc
- Thu nhap: Luong, thuong, phu cap, thu nhap, loi buon ban, tien lai
- Chua xac dinh: Cac giao dich khong ro rang hoac khong khop danh muc nao

LOAI GIAO DICH:
- Thu nhap: tien VAO (luong, thuong, qua tien, duoc cho, loi buon ban)
- Chi phi: tien RA (mua sam, thanh toan, an uong, di chuyen, dich vu)

QUY TAC SO TIEN:
- 1tr, 1 trieu = 1000000 VND
- 500k, 500 nghin = 500000 VND
- 50k = 50000 VND
- 1t, 1 ty = 1000000000 VND
- Giu nguyen so neu da la so
- Chi trich xuat SO DAU TIEN trong cau (giao dich chinh)

VI DU:
- Luong thang 10tr -> amount:10000000, category:Thu nhap, type:Thu nhap
- Di cho mua thuc pham 100000 -> amount:100000, category:An uong, type:Chi phi
- Xang xe 200k -> amount:200000, category:Di lai, type:Chi phi
- Tien nha tro 13362k -> amount:13362000, category:Nha o, type:Chi phi
- Lau 33000k -> amount:33000, category:An uong, type:Chi phi

QUY TAC OUTPUT:
- Chi tra JSON object, KHONG co text them
- category PHAI la mot trong: {CATEGORIES_STR}
- confidence: 1.0 = chac chan, 0.5 = khong chắc, 0.1 = doan

Vi du JSON: {{"amount": 1000000, "category": "Thu nhap", "type": "Thu nhap", "confidence": 0.95}}'''

# ==================== HELPER FUNCTIONS ====================
def load_json_data(filepath):
    """Load test data from JSON format"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    test_cases = []
    for item in data:
        for tx in item['transactions']:
            test_cases.append({
                'text': item['text'],
                'expected_amount': tx['amount'],
                'expected_category': tx['category'],
                'expected_type': tx['type']
            })
    return test_cases

def load_csv_data(filepath):
    """Load test data from CSV format"""
    test_cases = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_type = row["type"]
            mapped_type = "Chi phí" if raw_type == "Chi tiêu" else raw_type
            test_cases.append({
                "text": row["text"],
                "expected_amount": int(row["amount_vnd"]),
                "expected_category": row["category"],
                "expected_type": mapped_type
            })
    return test_cases

def parse_response(content):
    """Parse JSON from LLM response"""
    content = content.strip()
    
    # Handle markdown code blocks
    if content.startswith('```json'):
        content = content[7:-3]
    elif content.startswith('```'):
        content = content[3:-3]
    
    # Try to find JSON object
    content = content.strip()
    
    try:
    return json.loads(content)
    except json.JSONDecodeError:
        # Try to find JSON array
        start = content.find('[')
        end = content.rfind(']') + 1
        if start >= 0 and end > start:
            try:
                return json.loads(content[start:end])
            except:
                pass
        # Return empty dict as fallback
        return {}

def calculate_metrics(results, test_cases, categories):
    """Calculate all required metrics"""
    total = len(test_cases)
    
    # Basic counts
    cat_correct = sum(1 for r in results if r['cat_match'])
    type_correct = sum(1 for r in results if r['type_match'])
    amount_correct = sum(1 for r in results if r['amount_match'])
    all_correct = sum(1 for r in results if r['all_match'])
    
    # Build confusion data
    cat_true = defaultdict(list)
    cat_pred = defaultdict(list)
    
    for r, tc in zip(results, test_cases):
        cat_true[tc['expected_category']].append(1)
        if r['pred_category']:
        cat_pred[r['pred_category']].append(1)
    
    # Accuracy metrics
    metrics = {
        'total': total,
        'category_accuracy': cat_correct / total * 100 if total > 0 else 0,
        'type_accuracy': type_correct / total * 100 if total > 0 else 0,
        'amount_accuracy': amount_correct / total * 100 if total > 0 else 0,
        'exact_match_accuracy': all_correct / total * 100 if total > 0 else 0,
        'precisions_by_cat': {},
        'recalls_by_cat': {},
        'f1s_by_cat': {}
    }
    
    # Per-category Precision/Recall/F1
    precisions, recalls, f1s = [], [], []
    
    for cat in categories:
        tp = sum(1 for r, tc in zip(results, test_cases) 
                 if r['pred_category'] == cat and tc['expected_category'] == cat)
        
        pred_count = len([r for r in results if r['pred_category'] == cat])
        true_count = len(cat_true.get(cat, []))
        
        precision = tp / pred_count if pred_count > 0 else 0
        recall = tp / true_count if true_count > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        metrics['precisions_by_cat'][cat] = precision * 100
        metrics['recalls_by_cat'][cat] = recall * 100
        metrics['f1s_by_cat'][cat] = f1 * 100
        
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)
    
    # Macro averages
    metrics['macro_precision'] = sum(precisions) / len(precisions) * 100 if precisions else 0
    metrics['macro_recall'] = sum(recalls) / len(recalls) * 100 if recalls else 0
    metrics['macro_f1'] = sum(f1s) / len(f1s) * 100 if f1s else 0
    
    return metrics

def generate_report(metrics, results, errors, model_name, test_file, elapsed_time):
    """Generate evaluation report"""
    report = []
    report.append("=" * 80)
    report.append("           LLM TRANSACTION CLASSIFICATION - EVALUATION REPORT")
    report.append("=" * 80)
    report.append(f"Model:              {model_name}")
    report.append(f"Test File:          {test_file}")
    report.append(f"Total Test Cases:   {metrics['total']}")
    report.append(f"Evaluation Time:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Runtime:            {elapsed_time:.2f} seconds")
    report.append("")
    
    # Main metrics
    report.append("MAIN METRICS")
    report.append("-" * 80)
    report.append(f"{'Metric':<35} {'Value':>15}")
    report.append("-" * 80)
    report.append(f"{'Category Accuracy':<35} {metrics['category_accuracy']:>14.1f}%")
    report.append(f"{'Type Accuracy':<35} {metrics['type_accuracy']:>14.1f}%")
    report.append(f"{'Amount Accuracy':<35} {metrics['amount_accuracy']:>14.1f}%")
    report.append(f"{'Exact Match (All Correct)':<35} {metrics['exact_match_accuracy']:>14.1f}%")
    report.append("")
    
    # Classification metrics
    report.append("CLASSIFICATION METRICS (Macro-averaged)")
    report.append("-" * 80)
    report.append(f"{'Metric':<35} {'Value':>15}")
    report.append("-" * 80)
    report.append(f"{'Macro Precision':<35} {metrics['macro_precision']:>14.1f}%")
    report.append(f"{'Macro Recall':<35} {metrics['macro_recall']:>14.1f}%")
    report.append(f"{'Macro F1 Score':<35} {metrics['macro_f1']:>14.1f}%")
    report.append("")
    
    # Per-category performance
    report.append("PER-CATEGORY PERFORMANCE")
    report.append("-" * 80)
    report.append(f"{'Category':<20} {'Precision':>12} {'Recall':>12} {'F1 Score':>12} {'Support':>10}")
    report.append("-" * 80)
    
    for cat in sorted(metrics['f1s_by_cat'].keys()):
        p = metrics['precisions_by_cat'][cat]
        r = metrics['recalls_by_cat'][cat]
        f = metrics['f1s_by_cat'][cat]
        support = sum(1 for tc in results if tc['expected_category'] == cat)
        report.append(f"{cat:<20} {p:>11.1f}% {r:>11.1f}% {f:>11.1f}% {support:>10}")
    
    report.append("")
    
    # Target check
    report.append("TARGET CHECK (Target: 80%)")
    report.append("-" * 80)
    targets = [
        ('Category Accuracy', metrics['category_accuracy']),
        ('Type Accuracy', metrics['type_accuracy']),
        ('Amount Accuracy', metrics['amount_accuracy']),
        ('Macro Precision', metrics['macro_precision']),
        ('Macro Recall', metrics['macro_recall']),
        ('Macro F1 Score', metrics['macro_f1']),
    ]
    
    all_passed = True
    for name, value in targets:
        status = "PASS" if value >= 80 else "FAIL"
        if value < 80:
            all_passed = False
        report.append(f"{name:<35} {value:>14.1f}% - {status}")
    
    report.append("")
    if all_passed:
        report.append("TAT CA CAC CHI SO DAT >80% - DAT MUC TIEU!")
    else:
        report.append("CAN CAI THIEN THEM DE DAT >80%")
    
    report.append("")
    
    # Sample errors
    if errors:
        report.append("SAMPLE ERRORS (First 20)")
        report.append("-" * 80)
        for err in errors[:20]:
            report.append(f"Text: {err['text'][:60]}")
            if 'error' in err:
                report.append(f"  ERROR: {err['error']}")
            else:
                report.append(f"  Expected: category={err['expected_cat']}, type={err['expected_type']}, amount={err['expected_amt']}")
                report.append(f"  Predicted: category={err['pred_cat']}, type={err['pred_type']}, amount={err['pred_amt']}")
            report.append("")
    
    return "\n".join(report)

# ==================== MAIN EVALUATION ====================
def run_evaluation(sample_size=None, test_file=None, model_name=None, llm_url=None):
    """Run evaluation on test data"""
    # Set defaults
    test_file = test_file or DEFAULT_TEST_FILE
    model_name = model_name or DEFAULT_MODEL
    llm_url = llm_url or DEFAULT_LLM_URL
    
    print("=" * 70)
    print("LLM TRANSACTION CLASSIFICATION EVALUATION")
    print("=" * 70)
    print(f"Model: {model_name}")
    print(f"Test File: {test_file}")
    
    # Load test data
    if test_file.endswith('.json'):
        test_cases = load_json_data(test_file)
    else:
        test_cases = load_csv_data(test_file)
    
    print(f"Loaded {len(test_cases)} test cases")
    
    # Sample if needed
    if sample_size and sample_size < len(test_cases):
        import random
        random.seed(42)
        test_cases = random.sample(test_cases, sample_size)
        print(f"Sampled {sample_size} test cases")
    
    print()
    
    # Run evaluation
    headers = {'Content-Type': 'application/json'}
    results = []
    errors = []
    start_time = time.time()
    
    for i, case in enumerate(test_cases):
        try:
            user_prompt = f'Phan tich giao dich: "{case["text"]}"'
        
        data = {
                'model': model_name,
            'messages': [
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_prompt}
            ],
                'temperature': 0.1,
                'max_tokens': 200,
                'stream': False
        }
        
            response = requests.post(llm_url, headers=headers, json=data, timeout=60)
            elapsed = (time.time() - start_time) * 1000
            
            pred = parse_response(response.json().get('choices', [{}])[0].get('message', {}).get('content', ''))
            
            # Get first prediction if array
            if isinstance(pred, list) and len(pred) > 0:
                pred = pred[0]
            
            # Compare
            cat_match = pred.get('category') == case['expected_category']
            type_match = pred.get('type') == case['expected_type']
            amount_match = pred.get('amount') == case['expected_amount']
            all_match = cat_match and type_match and amount_match
            
            status = "OK" if all_match else "FAIL"
            
            if not all_match:
                errors.append({
                    'index': i + 1,
                    'text': case['text'],
                    'expected_cat': case['expected_category'],
                    'pred_cat': pred.get('category', 'ERROR'),
                    'expected_type': case['expected_type'],
                    'pred_type': pred.get('type', 'ERROR'),
                    'expected_amt': case['expected_amount'],
                    'pred_amt': pred.get('amount', 'ERROR')
                })
            
            results.append({
                'pred_category': pred.get('category'),
                'pred_type': pred.get('type'),
                'pred_amount': pred.get('amount'),
                'cat_match': cat_match,
                'type_match': type_match,
                'amount_match': amount_match,
                'all_match': all_match,
                'expected_category': case['expected_category'],
                'expected_type': case['expected_type'],
                'expected_amount': case['expected_amount']
                })
            
            print(f"[{i+1:3}/{len(test_cases)}] {status} | {case['text'][:40]:40} | {case['expected_category'][:10]:10} -> {pred.get('category', 'ERROR')[:10]:10}")
            
        except Exception as e:
            print(f"[{i+1:3}] ERROR: {str(e)[:50]}")
            errors.append({
                'index': i + 1,
                'text': case['text'],
                'error': str(e)
            })
            results.append({
                'pred_category': None,
                'pred_type': None,
                'pred_amount': None,
                'cat_match': False,
                'type_match': False,
                'amount_match': False,
                'all_match': False,
                'expected_category': case['expected_category'],
                'expected_type': case['expected_type'],
                'expected_amount': case['expected_amount']
            })
    
    elapsed_time = time.time() - start_time
    
    # Calculate metrics
    metrics = calculate_metrics(results, test_cases, DATASET_CATEGORIES)
    
    # Generate and print report
    report = generate_report(metrics, results, errors, model_name, test_file, elapsed_time)
    print("\n" + report)
    
    # Save report
    with open(DEFAULT_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nResults saved to: {DEFAULT_OUTPUT_FILE}")
    
    return metrics, results, errors

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate LLM for transaction classification')
    parser.add_argument('--sample', type=int, help='Number of samples to test')
    parser.add_argument('--file', type=str, help='Test file path (JSON or CSV)')
    parser.add_argument('--model', type=str, help='Model name')
    parser.add_argument('--url', type=str, help='LLM server URL')
    
    args = parser.parse_args()
    
    run_evaluation(
        sample_size=args.sample,
        test_file=args.file,
        model_name=args.model,
        llm_url=args.url
    )
