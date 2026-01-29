#!/usr/bin/env python3
"""Test accuracy script for transaction classification API."""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import csv
import requests
from typing import List, Dict, Any, Tuple
from collections import defaultdict

API_URL = "http://127.0.0.1:8000/api/v1/predict"

def load_test_data(csv_path: str, limit: int = 50) -> List[Dict[str, Any]]:
    """Load test data from CSV file."""
    test_cases = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            # Map "Chi tiêu" to "Chi phí" for API compatibility
            raw_type = row["type"]
            mapped_type = "Chi phí" if raw_type == "Chi tiêu" else raw_type
            
            test_cases.append({
                "text": row["text"],
                "expected_category": row["category"],
                "expected_type": mapped_type,
                "expected_amount": int(row["amount_vnd"])
            })
    return test_cases

def get_categories_from_data(test_cases: List[Dict[str, Any]]) -> List[str]:
    """Extract unique categories from test data."""
    categories = set()
    for case in test_cases:
        categories.add(case["expected_category"])
    return sorted(list(categories))

def call_api(text: str, categories: List[str]) -> Dict[str, Any]:
    """Call the prediction API."""
    payload = {
        "text": text,
        "categories": categories
    }
    response = requests.post(API_URL, json=payload, timeout=120)
    response.raise_for_status()
    return response.json()

def run_accuracy_test(test_cases: List[Dict[str, Any]], categories: List[str]) -> Dict[str, Any]:
    """Run accuracy test on all test cases."""
    results = {
        "total": len(test_cases),
        "category_correct": 0,
        "type_correct": 0,
        "amount_correct": 0,
        "all_correct": 0,
        "errors": []
    }
    
    print(f"\nModel: qwen2.5-7b-instruct-q4_k_m.gguf")
    print("\n" + "=" * 80)
    print(f"Testing {len(test_cases)} cases...")
    print("=" * 80 + "\n")
    
    for i, case in enumerate(test_cases):
        try:
            prediction = call_api(case["text"], categories)
            
            cat_match = prediction["category"] == case["expected_category"]
            type_match = prediction["type"] == case["expected_type"]
            amount_match = prediction["amount"] == case["expected_amount"]
            
            if cat_match:
                results["category_correct"] += 1
            if type_match:
                results["type_correct"] += 1
            if amount_match:
                results["amount_correct"] += 1
            if cat_match and type_match and amount_match:
                results["all_correct"] += 1
            
            status = "✅" if (cat_match and type_match and amount_match) else "❌"
            print(f"[{i+1:3}] {status} Text: {case['text'][:40]}...")
            print(f"      Expected: {case['expected_category']} | {case['expected_type']} | {case['expected_amount']:,}")
            print(f"      Predicted: {prediction['category']} | {prediction['type']} | {prediction['amount']:,} (conf: {prediction['confidence']:.2f})")
            
            if not (cat_match and type_match and amount_match):
                error_info = {
                    "text": case["text"],
                    "expected": {
                        "category": case["expected_category"],
                        "type": case["expected_type"],
                        "amount": case["expected_amount"]
                    },
                    "predicted": {
                        "category": prediction["category"],
                        "type": prediction["type"],
                        "amount": prediction["amount"]
                    }
                }
                results["errors"].append(error_info)
                
                if not cat_match:
                    print(f"      ⚠️  Category mismatch!")
                if not type_match:
                    print(f"      ⚠️  Type mismatch!")
                if not amount_match:
                    print(f"      ⚠️  Amount mismatch!")
            
            print()
            
        except Exception as e:
            print(f"[{i+1:3}] ❌ Error: {e}")
            results["errors"].append({
                "text": case["text"],
                "error": str(e)
            })
    
    return results

def print_summary(results: Dict[str, Any]):
    """Print test summary."""
    total = results["total"]
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total test cases: {total}")
    print()
    print(f"Category Accuracy: {results['category_correct']/total*100:.2f}% ({results['category_correct']}/{total})")
    print(f"Type Accuracy:     {results['type_correct']/total*100:.2f}% ({results['type_correct']}/{total})")
    print(f"Amount Accuracy:   {results['amount_correct']/total*100:.2f}% ({results['amount_correct']}/{total})")
    print(f"All Correct:       {results['all_correct']/total*100:.2f}% ({results['all_correct']}/{total})")
    print("=" * 80)

def print_error_analysis(results: Dict[str, Any]):
    """Print detailed error analysis."""
    errors = [e for e in results["errors"] if "predicted" in e]
    
    if not errors:
        print("\n✅ No errors to analyze!")
        return
    
    print(f"\n" + "=" * 80)
    print(f"ERROR ANALYSIS ({len(errors)} errors)")
    print("=" * 80)
    
    # Category confusion matrix
    cat_confusion = defaultdict(lambda: defaultdict(int))
    for error in errors:
        if error["expected"]["category"] != error["predicted"]["category"]:
            cat_confusion[error["expected"]["category"]][error["predicted"]["category"]] += 1
    
    print("\nMisclassifications by expected category:")
    for expected, predictions in sorted(cat_confusion.items()):
        pred_str = ", ".join([f"{pred}({count})" for pred, count in sorted(predictions.items(), key=lambda x: -x[1])])
        print(f"  {expected} → {pred_str}")

def main():
    csv_path = "data/test_3k.csv"
    
    # Load test data
    test_cases = load_test_data(csv_path, limit=50)
    print(f"Loaded {len(test_cases)} test cases")
    
    # Get categories from test data
    categories = get_categories_from_data(test_cases)
    print(f"Categories: {categories}")
    
    # Run test
    results = run_accuracy_test(test_cases, categories)
    
    # Print summary
    print_summary(results)
    
    # Print error analysis
    print_error_analysis(results)

if __name__ == "__main__":
    main()
