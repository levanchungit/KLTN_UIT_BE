#!/usr/bin/env python3
"""
Comprehensive LLM Test Script for Transaction Classification
Tests on 100-150 cases with full metrics: Accuracy, F1, Precision, Recall
Uses qwen2.5-7b model on port 8080
"""

import requests
import json
import sys
import time
import csv
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# CONFIG
LLM_URL = 'http://127.0.0.1:8080/v1/chat/completions'
MODEL_NAME = 'qwen2.5-7b-instruct-q4_k_m.gguf'
TEST_FILE = 'data/test_3k_aligned.csv'
OUTPUT_FILE = 'data/test_results.txt'

# Categories from dataset
CATEGORIES = ['4G', 'Cafe', 'Di chuyển', 'Giáo dục', 'Giải trí', 
              'Hớt tóc', 'Khác', 'Mượn tiền', 'Mỹ phẩm chăm sóc da', 
              'Phiếu lương', 'Quà tặng', 'Sức khỏe', 'Trả nợ', 'Tạp phẩm', 'Đám tiệc']
CATEGORIES_STR = ', '.join(f'"{cat}"' for cat in CATEGORIES)

SYSTEM_PROMPT = f'''Bạn là AI phân loại giao dịch tài chính cá nhân.

NHIỆM VỤ: Phân loại câu mô tả giao dịch thành category và type chính xác.

CATEGORIES (BẮT BUỘC chọn MỘT từ danh sách này):
{CATEGORIES_STR}

QUY TẮC PHÂN LOẠI:
- "4G": Internet/Data/Mobile/Wifi
- "Cafe": Đồ uống, trà, cà phê, sinh tố
- "Di chuyển": Xăng xe, taxi, bus, grab, di chuyển
- "Giáo dục": Học phí, sách vở, khóa học
- "Giải trí": Game, phim, giải trí, du lịch
- "Hớt tóc": Cắt tóc, làm đầu, salon
- "Khác": Không khớp category nào
- "Mượn tiền": Vay mượn tiền
- "Mỹ phẩm chăm sóc da": Sữa tắm, xà bông, mỹ phẩm, làm đẹp
- "Phiếu lương": Lương, thưởng, phụ cấp, thu nhập
- "Quà tặng": Quà tặng, được cho tiền
- "Sức khỏe": Thuốc, khám bệnh, y tế
- "Trả nợ": Trả nợ, thanh toán nợ
- "Tạp phẩm": Đồ dùng sinh hoạt, tạp hóa
- "Đám tiệc": Sinh nhật, đám cưới, tiệc tùng
- Nếu không khớp category nào → chọn "Khác"

TYPE (BẮT BUỘC):
- "Thu nhập": tiền vào (lương, thưởng, phụ cấp, quà tặng tiền, được cho, vay mượn)
- "Chi phí": tiền ra (mua sắm, thanh toán, ăn uống, di chuyển)

AMOUNT:
- "1tr", "1 triệu" = 1000000
- "500k", "500 nghìn" = 500000
- "50k" = 50000
- Giữ nguyên số nếu đã là số

OUTPUT: Chỉ trả JSON, KHÔNG có text thêm.
{{"amount": <số>, "category": "<ĐÚNG từ danh sách>", "type": "<Thu nhập hoặc Chi phí>", "confidence": <0-1>}}

VÍ DỤ:
  Input: "Cắt tóc 60k" → {{"amount": 60000, "category": "Hớt tóc", "type": "Chi phí", "confidence": 0.95}}
  Input: "Lương tháng 10tr" → {{"amount": 10000000, "category": "Phiếu lương", "type": "Thu nhập", "confidence": 0.95}}'''

def load_test_data(filepath):
    """Load test cases from CSV"""
    test_cases = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_type = row["type"]
            mapped_type = "Chi phí" if raw_type == "Chi tiêu" else raw_type
            test_cases.append({
                "text": row["text"],
                "expected_category": row["category"],
                "expected_type": mapped_type,
                "expected_amount": int(row["amount_vnd"])
            })
    return test_cases

def parse_response(content):
    """Parse JSON from LLM response"""
    content = content.strip()
    if content.startswith('```json'):
        content = content[7:-3]
    elif content.startswith('```'):
        content = content[3:-3]
    return json.loads(content)

def calculate_metrics(results, test_cases):
    """Calculate all required metrics"""
    total = len(test_cases)
    cat_correct = sum(1 for r in results if r['cat_match'])
    type_correct = sum(1 for r in results if r['type_match'])
    amount_correct = sum(1 for r in results if r['amount_match'])
    all_correct = sum(1 for r in results if r['all_match'])
    
    # Category-wise metrics for Precision/Recall/F1
    cat_true = defaultdict(list)
    cat_pred = defaultdict(list)
    for r, tc in zip(results, test_cases):
        cat_true[tc['expected_category']].append(1)
        cat_pred[r['pred_category']].append(1)
    
    # Overall accuracy
    category_acc = cat_correct / total * 100
    type_acc = type_correct / total * 100
    amount_acc = amount_correct / total * 100
    all_acc = all_correct / total * 100
    
    # Macro F1, Precision, Recall for categories
    precisions, recalls, f1s = [], [], []
    for cat in CATEGORIES:
        tp = sum(1 for r, tc in zip(results, test_cases) 
                 if r['pred_category'] == cat and tc['expected_category'] == cat)
        pred_count = len(cat_pred.get(cat, []))
        true_count = len(cat_true.get(cat, []))
        
        precision = tp / pred_count if pred_count > 0 else 0
        recall = tp / true_count if true_count > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)
    
    avg_precision = sum(precisions) / len(precisions) * 100
    avg_recall = sum(recalls) / len(recalls) * 100
    avg_f1 = sum(f1s) / len(f1s) * 100
    
    return {
        'category_accuracy': category_acc,
        'type_accuracy': type_acc,
        'amount_accuracy': amount_acc,
        'all_correct_accuracy': all_acc,
        'precision': avg_precision,
        'recall': avg_recall,
        'f1': avg_f1,
        'precisions_by_cat': dict(zip(CATEGORIES, precisions)),
        'recalls_by_cat': dict(zip(CATEGORIES, recalls)),
        'f1s_by_cat': dict(zip(CATEGORIES, f1s))
    }

def run_test():
    print("=" * 70)
    print(f"LLM ACCURACY TEST - QWEN2.5-1.5B")
    print(f"Model: {MODEL_NAME}")
    print("=" * 70)
    
    # Load test data
    test_cases = load_test_data(TEST_FILE)
    print(f"\nLoaded {len(test_cases)} test cases from {TEST_FILE}\n")
    
    headers = {'Content-Type': 'application/json'}
    results = []
    errors = []
    
    for i, case in enumerate(test_cases):
        user_prompt = f'"{case["text"]}" → JSON:'
        
        data = {
            'model': MODEL_NAME,
            'messages': [
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_prompt}
            ],
            'temperature': 0.0,
            'max_tokens': 200
        }
        
        start_time = time.time()
        try:
            r = requests.post(LLM_URL, headers=headers, json=data, timeout=30)
            elapsed = (time.time() - start_time) * 1000
            
            pred = parse_response(r.json().get('choices', [{}])[0].get('message', {}).get('content', ''))
            
            cat_match = pred.get("category") == case["expected_category"]
            type_match = pred.get("type") == case["expected_type"]
            amount_match = pred.get("amount") == case["expected_amount"]
            all_match = cat_match and type_match and amount_match
            
            results.append({
                'pred_category': pred.get('category', 'ERROR'),
                'pred_type': pred.get('type', 'ERROR'),
                'pred_amount': pred.get('amount', 0),
                'cat_match': cat_match,
                'type_match': type_match,
                'amount_match': amount_match,
                'all_match': all_match,
                'elapsed': elapsed,
                'text': case['text'],
                'expected_category': case['expected_category'],
                'expected_type': case['expected_type'],
                'expected_amount': case['expected_amount']
            })
            
            status = "✅" if all_match else "❌"
            if not all_match:
                errors.append({
                    'index': i + 1,
                    'text': case['text'],
                    'expected_cat': case['expected_category'],
                    'pred_cat': pred.get('category', 'ERROR'),
                    'expected_type': case['expected_type'],
                    'pred_type': pred.get('type', 'ERROR'),
                    'expected_amt': case['expected_amount'],
                    'pred_amt': pred.get('amount', 0)
                })
            
            print(f"[{i+1:3}] {status} {case['text'][:32]:32} | {case['expected_category'][:12]:12} → {pred.get('category', 'ERROR')[:12]} | {elapsed:.0f}ms")
            
        except Exception as e:
            print(f"[{i+1:3}] ❌ ERROR: {str(e)[:50]}")
            errors.append({
                'index': i + 1,
                'text': case['text'],
                'error': str(e)
            })
            results.append({
                'pred_category': 'ERROR',
                'pred_type': 'ERROR',
                'pred_amount': 0,
                'cat_match': False,
                'type_match': False,
                'amount_match': False,
                'all_match': False,
                'elapsed': 0,
                'text': case['text'],
                'expected_category': case['expected_category'],
                'expected_type': case['expected_type'],
                'expected_amount': case['expected_amount']
            })
    
    # Calculate metrics
    metrics = calculate_metrics(results, test_cases)
    
    # Build report
    report = []
    report.append("=" * 70)
    report.append("LLM TRANSACTION CLASSIFICATION - TEST RESULTS")
    report.append("=" * 70)
    report.append(f"Model: {MODEL_NAME}")
    report.append(f"Test File: {TEST_FILE}")
    report.append(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("MAIN METRICS")
    report.append("-" * 70)
    report.append(f"Total Test Cases:    {len(test_cases)}")
    report.append(f"Category Accuracy:   {metrics['category_accuracy']:.1f}%")
    report.append(f"Type Accuracy:       {metrics['type_accuracy']:.1f}%")
    report.append(f"Amount Accuracy:     {metrics['amount_accuracy']:.1f}%")
    report.append(f"All Correct (Exact): {metrics['all_correct_accuracy']:.1f}%")
    report.append("")
    report.append("CLASSIFICATION METRICS (Macro-averaged)")
    report.append("-" * 70)
    report.append(f"Precision:           {metrics['precision']:.1f}%")
    report.append(f"Recall:              {metrics['recall']:.1f}%")
    report.append(f"F1 Score:            {metrics['f1']:.1f}%")
    report.append("")
    report.append("PERFORMANCE")
    report.append("-" * 70)
    valid_times = [r['elapsed'] for r in results if r['elapsed'] > 0]
    if valid_times:
        report.append(f"Avg Response Time:   {sum(valid_times)/len(valid_times):.0f}ms")
        report.append(f"Min Response Time:   {min(valid_times):.0f}ms")
        report.append(f"Max Response Time:   {max(valid_times):.0f}ms")
    report.append("")
    
    # Category-wise metrics
    report.append("CATEGORY-WISE PERFORMANCE")
    report.append("-" * 70)
    for cat in CATEGORIES:
        p = metrics['precisions_by_cat'][cat] * 100
        r = metrics['recalls_by_cat'][cat] * 100
        f = metrics['f1s_by_cat'][cat] * 100
        report.append(f"{cat:20} | P: {p:5.1f}% | R: {r:5.1f}% | F1: {f:5.1f}%")
    report.append("")
    
    # Errors
    if errors:
        report.append("ERROR CASES")
        report.append("-" * 70)
        for err in errors[:30]:  # Show first 30 errors
            if 'error' in err:
                report.append(f"[{err['index']:3}] ERROR: {err['text'][:40]}")
            else:
                report.append(f"[{err['index']:3}] {err['text'][:35]:35}")
                report.append(f"     Expected: {err['expected_cat']:12} | Got: {err['pred_cat'][:12]:12}")
                report.append(f"     Type: {err['expected_type']:8} | Got: {err['pred_type'][:8]}")
                report.append(f"     Amt: {err['expected_amt']} | Got: {err['pred_amt']}")
        report.append(f"... and {len(errors) - 30} more errors" if len(errors) > 30 else "")
        report.append("")
    
    # Check targets
    report.append("TARGET CHECK")
    report.append("-" * 70)
    targets = [
        ("Category Accuracy", metrics['category_accuracy'], 80),
        ("Type Accuracy", metrics['type_accuracy'], 80),
        ("Amount Accuracy", metrics['amount_accuracy'], 80),
        ("Precision", metrics['precision'], 80),
        ("Recall", metrics['recall'], 80),
        ("F1 Score", metrics['f1'], 80),
    ]
    all_passed = True
    for name, value, target in targets:
        status = "✅ PASS" if value >= target else "❌ FAIL"
        if value < target:
            all_passed = False
        report.append(f"{name:20}: {value:5.1f}% (target: {target}%) - {status}")
    
    report.append("")
    if all_passed:
        report.append("✅ TAT CA CAC CHI SO DAT >80% - DAT MUC TIEU!")
    else:
        report.append("❌ CAN CAI THIEN THEM DE DAT >80%")
    
    report_text = "\n".join(report)
    
    # Print to console
    print("\n" + report_text)
    
    # Save to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    print(f"\nResults saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    run_test()
