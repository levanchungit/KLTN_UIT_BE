#!/usr/bin/env python
"""
Quick API test script for KLTN_UIT_BE
Tests health check and predict endpoints
"""
import sys
import time
import httpx

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("=" * 50)
    print("Testing /api/v1/health")
    print("=" * 50)
    
    response = httpx.get(f"{BASE_URL}/api/v1/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

def test_predict(text: str, categories: list = None):
    """Test predict endpoint"""
    print("\n" + "=" * 50)
    print(f"Testing /api/v1/predict")
    print(f"Input: '{text}'")
    print("=" * 50)
    
    payload = {
        "text": text,
        "categories": categories or []
    }
    
    start = time.time()
    response = httpx.post(
        f"{BASE_URL}/api/v1/predict",
        json=payload,
        timeout=60.0
    )
    elapsed = time.time() - start
    
    print(f"Status: {response.status_code}")
    print(f"Time: {elapsed:.2f}s")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Amount: {result.get('amount'):,} VND")
        print(f"Category: {result.get('category')}")
        print(f"Type: {result.get('type')}")
        print(f"Confidence: {result.get('confidence'):.2%}")
        if result.get('transactions'):
            print(f"Transactions: {len(result['transactions'])}")
            for tx in result['transactions']:
                print(f"  - {tx['item']}: {tx['amount']:,} VND ({tx['category']})")
    else:
        print(f"Error: {response.text}")
    
    return response.status_code == 200

def test_cache_stats():
    """Test cache stats endpoint"""
    print("\n" + "=" * 50)
    print("Testing /api/v1/cache/stats")
    print("=" * 50)
    
    response = httpx.get(f"{BASE_URL}/api/v1/cache/stats")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def main():
    print("\n[KLTN_UIT_BE API Test]\n")
    
    # Test health
    if not test_health():
        print("\n[X] Health check failed! Is the server running?")
        return
    
    # Test single transaction (open-domain)
    test_cases = [
        ("Grab di lam 45k", []),
        ("Me cho 1tr", []),
        ("Cafe sang 35k", []),
        ("Nhan luong thang 5 15tr", []),
        ("Kem 50k sua chua 42k tra dao 50k", []),  # Multi-transaction
    ]
    
    print("\n\n[Open-Domain Classification]")
    for text, categories in test_cases:
        test_predict(text, categories)
    
    # Test closed-domain
    print("\n\n[Closed-Domain Classification]")
    test_predict(
        "Grab di lam 45k",
        ["Di chuyen", "An uong", "Giai tri", "Khac"]
    )
    
    # Test cache stats
    test_cache_stats()
    
    print("\n\n[OK] All tests completed!")

if __name__ == "__main__":
    main()
