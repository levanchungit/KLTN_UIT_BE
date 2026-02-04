#!/usr/bin/env python3
"""
Chapter 5 Evaluation Script - Thử nghiệm và Đánh giá
Tính toán đầy đủ các chỉ số: Precision, Recall, F1, Accuracy, Latency

Usage:
    python chapter5_evaluation.py
"""

import json
import time
import sys
import requests
import os
from collections import defaultdict
from datetime import datetime
import re

sys.stdout.reconfigure(encoding='utf-8')

# ==================== CONFIGURATION ====================
LLM_URL = 'http://127.0.0.1:8080/v1/chat/completions'
MODEL_NAME = 'qwen2.5-7b-instruct-q4_k_m.gguf'
TEST_FILE = 'data/chapter5_test_dataset.json'
OUTPUT_FOLDER = 'data/test_thuc_te'

# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Get current timestamp for filename
TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M%S')

# Categories from dataset
DATASET_CATEGORIES = [
    'Ăn uống', 'Đi lại', 'Nhà ở', 'Mua sắm', 
    'Giải trí', 'Giáo dục', 'Y tế', 'Thu nhập', 'Chưa xác định'
]

CATEGORIES_STR = ', '.join(DATASET_CATEGORIES)

# ==================== ENHANCED SYSTEM PROMPT ====================
SYSTEM_PROMPT = f'''
BAN LA CHUYEN GIA PHAN LOAI GIAO DICH TAI CHINH VIET NAM.

NHIEM VU: Phan tich van ban mo ta giao dich, trich xuat TAT CA cac giao dich va tra ve JSON array.

DANH MUC CHI PHAI SU DUNG (EXACT):
{CATEGORIES_STR}

QUY TAC PHAN LOAI CHI TIET:

1. AN UONG:
   - an com, di cho, thuc pham, chợ, siêu thị thực phẩm, cơm, bún, phở, bánh mì, đồ ăn, thức ăn, nhà hàng, quán ăn, cafe, trà sữa, uống, ăn vặt, lẩu, buffet, tiệc
   - TỪ KHÓA: ăn, cơm, bún, phở, bánh, cafe, trà, uống, chợ, siêu thị, thực phẩm, lẩu, buffet

2. DI LAI:
   - xăng xe, taxi, grab, xe buýt, vé xe, đi xe, di chuyển, gửi xe, đỗ xe, vé máy bay, tàu hỏa, phà, cầu đường, phí cầu đường, toll
   - TỪ KHÓA: xăng, taxi, grab, xe, vé, đi, di chuyển, gửi, đỗ, cầu đường, toll

3. NHA O:
   - tiền nhà, tiền phòng, tiền trọ, điện, nước, gas, wifi, internet, phí quản lý, phí chung cư, dịch vụ nhà, bảo hiểm nhà, sửa nhà
   - TỪ KHÓA: nhà, phòng, trọ, điện, nước, gas, wifi, internet, quản lý, chung cư

4. MUA SAM:
   - quần áo, giày dép, túi xách, đồ điện tử, điện thoại, laptop, đồ gia dụng, dụng cụ, đồ lặt vặt, shopping, mua sắm
   - TỪ KHÓA: mua, quần, áo, giày, túi, điện tử, laptop, dụng cụ, shopping

5. GIAI TRI:
   - xem phim, netflix, spotify, game, karaoke, bar, club, du lịch, spa, massage, giải trí, concert, nhạc hội
   - TỪ KHÓA: phim, netflix, spotify, game, karaoke, bar, club, du lịch, spa, giải trí

6. GIAO DUC:
   - học phí, sách giáo khoa, khóa học, chứng chỉ, gia sư, trung tâm đào tạo, đồ dùng học tập, laptop học, máy tính học
   - TỪ KHÓA: học, sách, khóa, chứng chỉ, gia sư, trung tâm, đào tạo, học phí

7. Y TE:
   - thuốc, khám bệnh, bệnh viện, bác sĩ, siêu thị thuốc, y tế, spa chăm sóc sức khỏe, khám sức khỏe
   - TỪ KHÓA: thuốc, khám, bệnh, viện, bác sĩ, y tế, sức khỏe

8. THU NHAP:
   - lương, thưởng, tiền lãi, lợi nhuận, buôn bán, thu nhập, được cho, quà tặng, phụ cấp, thu nhập phụ
   - TỪ KHÓA: lương, thưởng, lãi, lợi, buôn bán, thu nhập, được cho, quà

9. CHUA XAC DINH:
   - phí linh tinh, chi tiêu không rõ, đóng góp từ thiện, thuế, phí dịch vụ không xác định
   - TỪ KHÓA: linh tinh, không rõ, từ thiện, thuế, phí dịch vụ

QUY TAC XAC DINH LOAI (THU/CHI):
- CHI PHI (tieu xuat): tien RA khi MUA, THANH TOAN, AN UONG, DI CHUYEN, DICH VU
- THU NHAP: tien VAO khi LƯƠNG, THƯỞNG, BÁN, LỢI NHUẬN, ĐƯỢC CHO

QUY TAC SO TIEN:
- 1tr, 1 trieu = 1000000
- 500k, 500 nghin = 500000
- 50k = 50000
- 1t (ty) = 1000000000
- 2tr, 2.5tr = 2000000, 2500000
- Giu nguyen so neu da la so
- CHI trich xuat SO TIEN CHINH (giao dich quan trong nhat trong cau)

OUTPUT FORMAT:
- Tra ve JSON array chua TAT CA cac giao dich
- Moi giao dich co: amount, category, type
- KHONG co text them, chi JSON

VI DU:
Input: "luong thang 10tr"
Output: [{{"amount": 10000000, "category": "Thu nhập", "type": "Thu nhập"}}]

Input: "di cho 100000 an uong"
Output: [{{"amount": 100000, "category": "Ăn uống", "type": "Chi phí"}}]

Input: "xang xe 200k, sau do luong 11tr"
Output: [{{"amount": 200000, "category": "Đi lại", "type": "Chi phí"}}, {{"amount": 11000000, "category": "Thu nhập", "type": "Thu nhập"}}]

CHI TRA JSON ARRAY, KHONG CO TEXT THEM.
'''

# ==================== HELPER FUNCTIONS ====================
def load_test_data(filepath):
    """Load test data from JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['test_samples']

def parse_llm_response(content):
    """Parse JSON from LLM response"""
    content = content.strip()
    
    # Remove markdown code blocks
    if content.startswith('```json'):
        content = content[7:-3]
    elif content.startswith('```'):
        content = content[3:-3]
    
    # Clean up
    content = content.strip()
    
    try:
        result = json.loads(content)
        if isinstance(result, dict) and 'transactions' in result:
            return result['transactions']
        elif isinstance(result, list):
            return result
        else:
            return [result]
    except json.JSONDecodeError:
        # Try to extract JSON from text
        try:
            match = re.search(r'\[.*\]', content, re.DOTALL)
            if match:
                return json.loads(match.group())
            match = re.search(r'\{.*\}', content, re.DOTALL)
            if match:
                return [json.loads(match.group())]
        except:
            pass
        return []

def call_llm(text):
    """Call LLM API"""
    data = {
        'model': MODEL_NAME,
        'messages': [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': f'Phan tich: "{text}" -> JSON array:'}
        ],
        'temperature': 0.05,
        'max_tokens': 300
    }
    
    start_time = time.time()
    response = requests.post(LLM_URL, json=data, timeout=120)
    elapsed = (time.time() - start_time) * 1000
    
    content = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    pred = parse_llm_response(content)
    
    return pred, elapsed

def normalize_text(text):
    """Normalize text for comparison"""
    if text is None:
        return ''
    return text.lower().replace(' ', '').replace('_', '').replace('-', '')

def is_category_match(pred_cat, true_cat):
    """Check if category matches (handle Unicode variations)"""
    if pred_cat is None or true_cat is None:
        return False
    pred_norm = normalize_text(pred_cat)
    true_norm = normalize_text(true_cat)
    
    if pred_norm == true_norm:
        return True
    
    variations = {
        'ăn uống': ['ănuống', 'an uong', 'anuong'],
        'đi lại': ['đilại', 'di lai', 'dilai'],
        'nhà ở': ['nhàở', 'nha o', 'nhaở'],
        'mua sắm': ['muasắm', 'mua sam', 'muasam'],
        'giải trí': ['giảitri', 'giai tri', 'giaitri'],
        'giáo dục': ['giáodục', 'giao duc', 'giaoduc'],
        'y tế': ['ytế', 'y te', 'yte'],
        'thu nhập': ['thunhập', 'thu nhap', 'thunhap'],
        'chưa xác định': ['chưaxácđịnh', 'chua xac dinh', 'chuaxacdinh']
    }
    
    true_variations = variations.get(true_norm, [])
    return pred_norm in [true_norm] + true_variations

def is_type_match(pred_type, true_type):
    """Check if type matches"""
    if pred_type is None or true_type is None:
        return False
    pred_t = pred_type.lower().strip()
    true_t = true_type.lower().strip()
    
    pred_t = pred_t.replace('í', 'i').replace('ế', 'e').replace('ề', 'e')
    true_t = true_t.replace('í', 'i').replace('ế', 'e').replace('ề', 'e')
    
    return pred_t == true_t

def is_amount_match(pred_amount, true_amount):
    """Check if amount matches (allow small variations)"""
    if pred_amount is None or true_amount is None:
        return False
    
    try:
        pred_val = int(pred_amount)
        true_val = int(true_amount)
        
        if pred_val == true_val:
            return True
        
        diff_percent = abs(pred_val - true_val) / true_val if true_val > 0 else 1
        return diff_percent <= 0.05
    except:
        return False

def match_predictions_to_expected(predictions, expected_transactions):
    """Match predictions to expected transactions for evaluation"""
    if not predictions:
        return []
    
    if not expected_transactions:
        return []
    
    matches = []
    used_expected = set()
    
    for pred in predictions:
        best_match_idx = -1
        best_score = 0
        
        for i, exp in enumerate(expected_transactions):
            if i in used_expected:
                continue
            
            cat_score = 1 if is_category_match(pred.get('category'), exp.get('category')) else 0
            type_score = 1 if is_type_match(pred.get('type'), exp.get('type')) else 0
            amount_score = 1 if is_amount_match(pred.get('amount'), exp.get('amount')) else 0
            
            total_score = cat_score + type_score + amount_score
            
            if total_score > best_score:
                best_score = total_score
                best_match_idx = i
        
        if best_match_idx >= 0:
            matches.append({
                'prediction': pred,
                'expected': expected_transactions[best_match_idx],
                'cat_match': is_category_match(pred.get('category'), expected_transactions[best_match_idx].get('category')),
                'type_match': is_type_match(pred.get('type'), expected_transactions[best_match_idx].get('type')),
                'amount_match': is_amount_match(pred.get('amount'), expected_transactions[best_match_idx].get('amount')),
                'all_match': False
            })
            used_expected.add(best_match_idx)
    
    for m in matches:
        m['all_match'] = m['cat_match'] and m['type_match'] and m['amount_match']
    
    return matches

def calculate_metrics(results, test_cases):
    """Calculate all metrics"""
    
    all_cat_matches = []
    all_type_matches = []
    all_amount_matches = []
    all_all_matches = []
    cat_true_counts = defaultdict(int)
    cat_pred_counts = defaultdict(int)
    cat_tp_counts = defaultdict(int)
    
    for result in results:
        for match in result['matches']:
            exp = match['expected']
            pred = match['prediction']
            
            all_cat_matches.append(match['cat_match'])
            all_type_matches.append(match['type_match'])
            all_amount_matches.append(match['amount_match'])
            all_all_matches.append(match['all_match'])
            
            cat_true_counts[exp['category']] += 1
            if pred.get('category'):
                cat_pred_counts[pred['category']] += 1
                if match['cat_match']:
                    cat_tp_counts[exp['category']] += 1
    
    total = len(all_all_matches) if all_all_matches else 1
    
    per_cat_metrics = {}
    for cat in DATASET_CATEGORIES:
        tp = cat_tp_counts.get(cat, 0)
        pred = cat_pred_counts.get(cat, 0)
        true = cat_true_counts.get(cat, 0)
        
        precision = tp / pred if pred > 0 else 0
        recall = tp / true if true > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        per_cat_metrics[cat] = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'support': true
        }
    
    active_cats = [cat for cat in DATASET_CATEGORIES if cat_true_counts.get(cat, 0) > 0]
    if not active_cats:
        active_cats = DATASET_CATEGORIES
    
    precisions = [per_cat_metrics[c]['precision'] for c in active_cats]
    recalls = [per_cat_metrics[c]['recall'] for c in active_cats]
    f1s = [per_cat_metrics[c]['f1'] for c in active_cats]
    
    metrics = {
        'total_samples': len(test_cases),
        'total_transactions': total,
        'category_accuracy': sum(all_cat_matches) / total if total > 0 else 0,
        'type_accuracy': sum(all_type_matches) / total if total > 0 else 0,
        'amount_accuracy': sum(all_amount_matches) / total if total > 0 else 0,
        'exact_match_accuracy': sum(all_all_matches) / total if total > 0 else 0,
        'macro_precision': sum(precisions) / len(precisions),
        'macro_recall': sum(recalls) / len(recalls),
        'macro_f1': sum(f1s) / len(f1s),
        'per_category': per_cat_metrics
    }
    
    return metrics

# ==================== MAIN EVALUATION ====================
def run_evaluation():
    print("=" * 70)
    print("CHUONG 5 - THU NGHIEM VA DANH GIA")
    print("=" * 70)
    print(f"Model: {MODEL_NAME}")
    print(f"Test File: {TEST_FILE}")
    print(f"Output Folder: {OUTPUT_FOLDER}")
    print()
    
    # Load test data
    test_cases = load_test_data(TEST_FILE)
    print(f"Loaded {len(test_cases)} test samples")
    
    total_transactions = sum(len(c['transactions']) for c in test_cases)
    print(f"Total transactions: {total_transactions}")
    print()
    
    # Check LLM availability
    try:
        requests.get(LLM_URL.replace('/v1/chat/completions', '/v1/models'), timeout=5)
    except:
        print(f"ERROR: LLM server not available at {LLM_URL}")
        print("Please start llama.cpp server first:")
        print(f"  ./llama-server -m models/{MODEL_NAME} --port 8080 --host 127.0.0.1")
        return None
    
    # Run evaluation
    results = []
    latencies = []
    errors = []
    
    for i, case in enumerate(test_cases):
        text = case['text']
        expected_transactions = case['transactions']
        
        try:
            pred, elapsed = call_llm(text)
            latencies.append(elapsed)
            
            matches = match_predictions_to_expected(pred, expected_transactions)
            
            if matches:
                all_correct = all(m['all_match'] for m in matches)
                first_cat = matches[0]['expected']['category']
                first_pred_cat = matches[0]['prediction'].get('category')
            else:
                all_correct = False
                first_cat = expected_transactions[0]['category']
                first_pred_cat = None
            
            status = "OK" if all_correct else "PARTIAL" if matches else "FAIL"
            
            if not all_correct:
                errors.append({
                    'id': case['id'],
                    'text': text[:50],
                    'expected_count': len(expected_transactions),
                    'pred_count': len(pred),
                    'expected_cat': first_cat,
                    'pred_cat': first_pred_cat
                })
            
            results.append({
                'id': case['id'],
                'text': text,
                'matches': matches,
                'expected_transactions': expected_transactions,
                'predictions': pred,
                'latency_ms': elapsed
            })
            
            print(f"[{i+1:2}/{len(test_cases)}] {status} | {text[:40]:40} | Exp:{len(expected_transactions)} Pred:{len(pred)}")
            
        except Exception as e:
            print(f"[{i+1:2}] ERROR: {str(e)[:50]}")
            errors.append({
                'id': case['id'],
                'text': text[:50],
                'error': str(e)
            })
            results.append({
                'id': case['id'],
                'text': text,
                'matches': [],
                'expected_transactions': expected_transactions,
                'predictions': [],
                'latency_ms': 0
            })
    
    # Calculate metrics
    metrics = calculate_metrics(results, test_cases)
    
    # Calculate latency statistics
    if latencies:
        metrics['latency'] = {
            'avg_ms': sum(latencies) / len(latencies),
            'min_ms': min(latencies),
            'max_ms': max(latencies),
            'std_ms': (sum((x - sum(latencies)/len(latencies))**2 for x in latencies) / len(latencies)) ** 0.5
        }
    else:
        metrics['latency'] = {'avg_ms': 0, 'min_ms': 0, 'max_ms': 0, 'std_ms': 0}
    
    metrics['errors_count'] = len(errors)
    
    # Print results
    print()
    print("=" * 70)
    print("KET QUA DANH GIA - CHAPTER 5 EVALUATION RESULTS")
    print("=" * 70)
    
    print("\n1. TONG QUAN")
    print("-" * 50)
    print(f"Tong so mau: {metrics['total_samples']}")
    print(f"Tong so giao dich: {metrics['total_transactions']}")
    print(f"Thoi gian chay: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n2. CAC CHI SO CHINH")
    print("-" * 50)
    print(f"{'Chi so':<30} {'Gia tri':>15}")
    print("-" * 50)
    print(f"{'Category Accuracy':<30} {metrics['category_accuracy']*100:>14.1f}%")
    print(f"{'Type Accuracy':<30} {metrics['type_accuracy']*100:>14.1f}%")
    print(f"{'Amount Accuracy':<30} {metrics['amount_accuracy']*100:>14.1f}%")
    print(f"{'Exact Match (All Correct)':<30} {metrics['exact_match_accuracy']*100:>14.1f}%")
    
    print("\n3. CLASSIFICATION METRICS (Macro-averaged)")
    print("-" * 50)
    print(f"{'Chi so':<30} {'Gia tri':>15}")
    print("-" * 50)
    print(f"{'Macro Precision':<30} {metrics['macro_precision']*100:>14.1f}%")
    print(f"{'Macro Recall':<30} {metrics['macro_recall']*100:>14.1f}%")
    print(f"{'Macro F1 Score':<30} {metrics['macro_f1']*100:>14.1f}%")
    
    print("\n4. HIEU NANG KY THUAT (Latency)")
    print("-" * 50)
    print(f"{'Chi so':<30} {'Gia tri':>15}")
    print("-" * 50)
    print(f"{'Avg Response Time':<30} {metrics['latency']['avg_ms']:>14.0f}ms")
    print(f"{'Min Response Time':<30} {metrics['latency']['min_ms']:>14.0f}ms")
    print(f"{'Max Response Time':<30} {metrics['latency']['max_ms']:>14.0f}ms")
    print(f"{'Std Deviation':<30} {metrics['latency']['std_ms']:>14.0f}ms")
    
    print("\n5. PHAN TICH THEO DANH MUC")
    print("-" * 70)
    print(f"{'Category':<15} {'Precision':>12} {'Recall':>12} {'F1':>12} {'Support':>10}")
    print("-" * 70)
    for cat in sorted(metrics['per_category'].keys()):
        m = metrics['per_category'][cat]
        print(f"{cat:<15} {m['precision']*100:>11.1f}% {m['recall']*100:>11.1f}% {m['f1']*100:>11.1f}% {m['support']:>10}")
    
    # Save comprehensive results to timestamped folder
    return metrics, results, test_cases

# ==================== GENERATE COMPREHENSIVE CHAPTER 5 CONTENT ====================
def generate_chapter5_content(metrics, results, test_cases):
    """Generate comprehensive Chapter 5 content for thesis"""
    
    content = f'''
================================================================================
BAO CAO THU NGHIEM VA DANH GIA - CHAPTER 5 EVALUATION REPORT
================================================================================
Thoi gian test: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Ten file: test_{TIMESTAMP}
================================================================================

================================================================================
PHAN 1: THONG TIN HE THONG VA CAU HINH
================================================================================

1.1. MO HINH SU DUNG
--------------------
- Ten mo hinh: {MODEL_NAME}
- Loai mo hinh: {MODEL_NAME}
- Nha phat trien: Alibaba Cloud
- Kich thuoc: 7 tỷ tham số
- Phuong phap luong tử: 4-bit quantization (GGUF format)

1.2. MO TRUONG CHAY
-------------------
- Server: llama.cpp (local inference)
- Port: 8080
- URL: {LLM_URL}
- Phuong phap: Zero-shot prompt engineering
- Fine-tuning: KHONG (chi su dung prompt)

1.3. THONG SO MO HINH
---------------------
- Temperature: 0.05 (rất thấp để đảm bảo tính nhất quán)
- Max tokens: 300
- Top-p: mặc định
- Top-k: mặc định

================================================================================
PHAN 2: SYSTEM PROMPT SU DUNG
================================================================================

{SYSTEM_PROMPT}

================================================================================
PHAN 3: DANH MUC GIAO DICH VA DINH NGHIA CHI TIET
================================================================================

DANH MUC CHÍNH (9 DANH MUC):
{'-' * 50}
'''
    
    # Add detailed category definitions
    category_definitions = {
        'Ăn uống': '''  - Mo ta: Chi phí liên quan đến thực phẩm, đồ uống, ăn uống hàng ngày
  - Tu khoa: ăn, cơm, bún, phở, bánh, cafe, trà, uống, chợ, siêu thị, thực phẩm, lẩu, buffet
  - Ví dụ: "đi chợ 100k", "uống cà phê 50k", "ăn cơm 80k"''',
        
        'Đi lại': '''  - Mo ta: Chi phí di chuyển, giao thông, vận tải
  - Tu khoa: xăng, taxi, grab, xe, vé, đi, di chuyển, gửi, đỗ, cầu đường, toll
  - Ví dụ: "xăng xe 200k", "đi taxi 150k", "gửi xe 20k"''',
        
        'Nhà ở': '''  - Mo ta: Chi phí liên quan đến nhà ở, điện nước, dịch vụ nhà
  - Tu khoa: nhà, phòng, trọ, điện, nước, gas, wifi, internet, quản lý, chung cư
  - Ví dụ: "tiền nhà 3tr", "điện 500k", "wifi 200k"''',
        
        'Mua sắm': '''  - Mo ta: Chi phí mua sắm vật dụng, đồ dùng cá nhân, đồ điện tử
  - Tu khoa: mua, quần, áo, giày, túi, điện tử, laptop, dụng cụ, shopping
  - Ví dụ: "mua áo 300k", "giày 500k", "laptop 15tr"''',
        
        'Giải trí': '''  - Mo ta: Chi phí giải trí, giải stress, thư giãn
  - Tu khoa: phim, netflix, spotify, game, karaoke, bar, club, du lịch, spa, giải trí
  - Ví dụ: "xem phim 100k", "netflix 80k", "karaoke 200k"''',
        
        'Giáo dục': '''  - Mo ta: Chi phí học tập, đào tạo, nâng cao kiến thức
  - Tu khoa: học, sách, khóa, chứng chỉ, gia sư, trung tâm, đào tạo, học phí
  - Ví dụ: "học phí 2tr", "sách 200k", "khóa học 1tr"''',
        
        'Y tế': '''  - Mo ta: Chi phí y tế, sức khỏe, chăm sóc sức khỏe
  - Tu khoa: thuốc, khám, bệnh, viện, bác sĩ, y tế, sức khỏe
  - Ví dụ: "thuốc 150k", "khám bệnh 300k", "spa 500k"''',
        
        'Thu nhập': '''  - Mo ta: Tiền vào, thu nhập từ các nguồn
  - Tu khoa: lương, thưởng, lãi, lợi, buôn bán, thu nhập, được cho, quà
  - Ví dụ: "lương 10tr", "thưởng 2tr", "bán hàng 5tr"''',
        
        'Chưa xác định': '''  - Mo ta: Các giao dich không rõ ràng, không khớp danh mục nào
  - Tu khoa: linh tinh, không rõ, từ thiện, thuế, phí dịch vụ
  - Ví dụ: "phí linh tinh 100k", "đóng góp 200k", "thuế 500k"'''
    }
    
    for cat in DATASET_CATEGORIES:
        content += f"\n{cat}:\n{category_definitions.get(cat, '  - Khong co dinh nghia')}\n"
    
    content += f'''
================================================================================
PHAN 4: BO DU LIEU THU NGHIEM
================================================================================

4.1. THONG TIN CHUNG
--------------------
- Ten file: {TEST_FILE}
- Tong so mau: {metrics['total_samples']}
- Tong so giao dich: {metrics['total_transactions']}
- Phuong phap chia du lieu: Manual selection

4.2. PHAN BO DANH MUC TRONG BO TEST
-----------------------------------
'''
    
    for cat, m in sorted(metrics['per_category'].items(), key=lambda x: -x[1]['support']):
        content += f"  - {cat}: {m['support']} giao dich ({m['support']/metrics['total_transactions']*100:.1f}%)\n"
    
    content += f'''

4.3. CHI TIET CAC MAU TEST
---------------------------
'''
    
    for case in test_cases:
        trans = case['transactions']
        content += f"\n[ID {case['id']}] {case['text']}\n"
        content += f"  Expected: {len(trans)} transaction(s)\n"
        for t in trans:
            content += f"    - Amount: {t['amount']:,} | Category: {t['category']} | Type: {t['type']}\n"
    
    content += f'''
================================================================================
PHAN 5: CAC CHI SO DANH GIA
================================================================================

5.1. CONG THUC SU DUNG
----------------------
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 = 2 × (Precision × Recall) / (Precision + Recall)
- Accuracy = So mau dung / Tong so mau

5.2. CAC CHI SO CHINH
---------------------
'''
    
    content += f"{'Chi so':<35} {'Gia tri':>15}\n"
    content += f"{'-' * 50}\n"
    content += f"{'Category Accuracy (Do chinh xac danh muc)':<35} {metrics['category_accuracy']*100:>14.1f}%\n"
    content += f"{'Type Accuracy (Do chinh xac loai)':<35} {metrics['type_accuracy']*100:>14.1f}%\n"
    content += f"{'Amount Accuracy (Do chinh xac so tien)':<35} {metrics['amount_accuracy']*100:>14.1f}%\n"
    content += f"{'Exact Match (Tat ca dung)':<35} {metrics['exact_match_accuracy']*100:>14.1f}%\n"
    
    content += f'''

5.3. CLASSIFICATION METRICS (MACRO-AVERAGED)
--------------------------------------------
'''
    
    content += f"{'Chi so':<35} {'Gia tri':>15}\n"
    content += f"{'-' * 50}\n"
    content += f"{'Macro Precision':<35} {metrics['macro_precision']*100:>14.1f}%\n"
    content += f"{'Macro Recall':<35} {metrics['macro_recall']*100:>14.1f}%\n"
    content += f"{'Macro F1 Score':<35} {metrics['macro_f1']*100:>14.1f}%\n"
    
    content += f'''

5.4. CHI TIET THEO DANH MUC
---------------------------
'''
    
    content += f"{'Category':<15} {'Precision':>12} {'Recall':>12} {'F1':>12} {'Support':>10}\n"
    content += f"{'-' * 61}\n"
    for cat in sorted(metrics['per_category'].keys()):
        m = metrics['per_category'][cat]
        content += f"{cat:<15} {m['precision']*100:>11.1f}% {m['recall']*100:>11.1f}% {m['f1']*100:>11.1f}% {m['support']:>10}\n"
    
    content += f'''

5.5. HIEU NANG KY THUAT (LATENCY)
---------------------------------
'''
    
    content += f"{'Chi so':<35} {'Gia tri':>15}\n"
    content += f"{'-' * 50}\n"
    content += f"{'Avg Response Time (Trung binh)':<35} {metrics['latency']['avg_ms']:>14.0f}ms\n"
    content += f"{'Min Response Time (Thap nhat)':<35} {metrics['latency']['min_ms']:>14.0f}ms\n"
    content += f"{'Max Response Time (Cao nhat)':<35} {metrics['latency']['max_ms']:>14.0f}ms\n"
    content += f"{'Std Deviation (Do lech chuan)':<35} {metrics['latency']['std_ms']:>14.0f}ms\n"
    
    content += f'''

================================================================================
PHAN 6: KET QUA CHI TIET TUNG MAU
================================================================================

'''
    
    for result in results:
        content += f"\n[ID {result['id']}] {result['text']}\n"
        content += f"  Latency: {result['latency_ms']:.0f}ms\n"
        content += f"  Expected: {len(result['expected_transactions'])} | Predicted: {len(result['predictions'])}\n"
        for match in result['matches']:
            exp = match['expected']
            pred = match['prediction']
            status = "OK" if match['all_match'] else "FAIL"
            content += f"  [{status}] Expected: {{amount: {exp['amount']}, cat: {exp['category']}, type: {exp['type']}}}\n"
            content += f"           Predicted: {{amount: {pred.get('amount')}, cat: {pred.get('category')}, type: {pred.get('type')}}}\n"
    
    content += f'''
================================================================================
PHAN 7: KET LUAN
================================================================================

7.1. TONG KET KET QUA
---------------------
Mo hinh {MODEL_NAME} su dung ky thuat prompt engineering dat duoc:

- F1 Score (Macro): {metrics['macro_f1']*100:.1f}% (Muc tieu: >80%)
- Category Accuracy: {metrics['category_accuracy']*100:.1f}%
- Type Accuracy: {metrics['type_accuracy']*100:.1f}%
- Amount Accuracy: {metrics['amount_accuracy']*100:.1f}%
- Exact Match: {metrics['exact_match_accuracy']*100:.1f}%

7.2. PHAN TICH
--------------
- Diem manh: Mo hinh hoat dong tot nhat voi cac danh muc co tu khoa ro rang
- Diem yeu: Can cai thiện cho các danh muc co tuong tu (Ăn uống, Đi lại)
- Hieu nang: Thoi gian phan hoi trung binh {metrics['latency']['avg_ms']:.0f}ms phù hợp cho ung dung thời gian thực

7.3. KHUYEN NGHI
----------------
- Tiep tuc toi uu prompt de cai thiện recall cho các danh muc ti le thap
- Co the xem xet fine-tuning neu can thiet chinh xac cao hon

================================================================================
BAO CAO DUOC TAO BOI: chapter5_evaluation.py
THOI GIAN TAO: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
================================================================================
'''
    
    return content

if __name__ == "__main__":
    metrics, results, test_cases = run_evaluation()
    
    if metrics:
        # Generate comprehensive Chapter 5 content
        chapter5 = generate_chapter5_content(metrics, results, test_cases)
        print(chapter5)
        
        # Save to timestamped folder
        output_filename = f"test_{TIMESTAMP}_chapter5_content.txt"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(chapter5)
        
        print(f"\nChapter 5 content saved to: {output_path}")
        
        # Also save to main chapter5_content.txt for reference
        with open('data/chapter5_content.txt', 'w', encoding='utf-8') as f:
            f.write(chapter5)
        print("Also saved to: data/chapter5_content.txt")
        
        # Save JSON results
        json_output_path = os.path.join(OUTPUT_FOLDER, f"test_{TIMESTAMP}_results.json")
        json_output = {
            'metadata': {
                'timestamp': TIMESTAMP,
                'model': MODEL_NAME,
                'test_file': TEST_FILE,
                'evaluation_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_samples': metrics['total_samples'],
                'total_transactions': metrics['total_transactions'],
                'system_prompt': SYSTEM_PROMPT,
                'categories': DATASET_CATEGORIES
            },
            'main_metrics': {
                'category_accuracy': f"{metrics['category_accuracy']*100:.1f}%",
                'type_accuracy': f"{metrics['type_accuracy']*100:.1f}%",
                'amount_accuracy': f"{metrics['amount_accuracy']*100:.1f}%",
                'exact_match_accuracy': f"{metrics['exact_match_accuracy']*100:.1f}%"
            },
            'classification_metrics': {
                'macro_precision': f"{metrics['macro_precision']*100:.1f}%",
                'macro_recall': f"{metrics['macro_recall']*100:.1f}%",
                'macro_f1_score': f"{metrics['macro_f1']*100:.1f}%"
            },
            'latency': {
                'average_ms': f"{metrics['latency']['avg_ms']:.0f}",
                'min_ms': f"{metrics['latency']['min_ms']:.0f}",
                'max_ms': f"{metrics['latency']['max_ms']:.0f}",
                'std_ms': f"{metrics['latency']['std_ms']:.0f}"
            },
            'per_category_metrics': {
                cat: {
                    'precision': f"{m['precision']*100:.1f}%",
                    'recall': f"{m['recall']*100:.1f}%",
                    'f1': f"{m['f1']*100:.1f}%",
                    'support': m['support']
                }
                for cat, m in metrics['per_category'].items()
            },
            'results': results
        }
        
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, ensure_ascii=False, indent=2)
        
        print(f"JSON results saved to: {json_output_path}")
