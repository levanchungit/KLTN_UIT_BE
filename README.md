# KLTN_UIT_BE - AI Backend for Transaction Classification

FastAPI + llama.cpp Integration với Qwen2.5-7B

## Mục tiêu

Xây dựng dịch vụ AI Backend nhận mô tả giao dịch tiếng Việt từ React Native, gọi LLM (Qwen chạy bằng llama.cpp) để trích xuất số tiền + phân loại danh mục, trả về JSON:

```json
{
  "amount": 1000000,
  "category": "Quà tặng",
  "type": "Thu nhập",
  "confidence": 0.88
}
```

## Kiến trúc hệ thống

```
┌─────────────────────────────────────────────────────────────────┐
│                      KLTN_UIT (Frontend)                         │
│  User nhập: "Sáng nay uống cafe 50k, chiều đi grab 80k"          │
└──────────────────────────┬──────────────────────────────────────┘
                           │ POST /api/v1/predict
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   KLTN_UIT_BE (FastAPI Backend)                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  1. Preprocessing: Chuẩn hóa text tiếng Việt             │   │
│  │  2. LLM Service: Gọi llama.cpp server                    │   │
│  │  3. Postprocessing: Parse JSON + Validate                │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────────┘
                           │ HTTP POST /v1/chat/completions
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    llama.cpp Server (Qwen2.5-7B)                 │
│  Model: qwen2.5-7b-instruct-q4_k_m.gguf                          │
│  Port: 8080                                                      │
└─────────────────────────────────────────────────────────────────┘
```

## Cài đặt nhanh

### 1. Cài đặt dependencies

```bash
cd KLTN_UIT_BE
pip install -r requirements.txt
```

### 2. Khởi động LLM Server (llama.cpp)

```bash
# Di chuyển đến thư mục llama.cpp
cd ../llama.cpp

# Khởi động server với Qwen2.5-7B
./llama-server -m models/qwen2.5-7b-instruct-q4_k_m.gguf --port 8080 --host 127.0.0.1 -c 2048
```

### 3. Khởi động FastAPI Backend

```bash
cd KLTN_UIT_BE

# Development mode (với hot reload)
python -m app.main

# Hoặc
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Test nhanh

```bash
# Chạy quick evaluation (30 test cases)
python quick_eval.py

# Hoặc chuẩn bị data và chạy full evaluation
python prepare_data.py
python test_llm_7b_direct.py --file data/evaluation/aligned_test_100.csv
```

## Đánh giá Model (F1 Score, Precision, Recall)

### Chuẩn bị dữ liệu

```bash
# Phân tích và chuẩn bị dữ liệu đánh giá
python prepare_data.py
```

Script này sẽ:
- Phân tích dataset (`training_data.json`, `test_data.json`)
- Tạo file CSV aligned cho evaluation
- Tạo `data/evaluation/aligned_test_100.csv` (100 mẫu test nhanh)
- Tạo `data/evaluation/aligned_test.csv` (toàn bộ test set)

### Chạy Evaluation

```bash
# Test nhanh với 100 mẫu
python test_llm_7b_direct.py --file data/evaluation/aligned_test_100.csv

# Test đầy đủ với toàn bộ test set
python test_llm_7b_direct.py --file data/evaluation/aligned_test.csv

# Test với số lượng tùy chỉnh
python test_llm_7b_direct.py --sample 50 --file data/evaluation/aligned_test.csv
```

### Kết quả Evaluation

Script sẽ xuất report bao gồm:

| Metric | Mô tả | Mục tiêu |
|--------|-------|----------|
| Category Accuracy | % dự đoán đúng category | ≥ 80% |
| Type Accuracy | % dự đoán đúng loại (thu/chi) | ≥ 90% |
| Amount Accuracy | % dự đoán đúng số tiền | ≥ 90% |
| Macro Precision | Precision trung bình theo category | ≥ 80% |
| Macro Recall | Recall trung bình theo category | ≥ 80% |
| **Macro F1** | **2×P×R/(P+R) - chỉ số chính** | **≥ 80%** |

### Ví dụ Output

```
================================================================================
           LLM TRANSACTION CLASSIFICATION - EVALUATION REPORT
================================================================================
Model:              qwen2.5-7b-instruct-q4_k_m.gguf
Test File:          data/evaluation/aligned_test_100.csv
Total Test Cases:   100
Evaluation Time:    2024-01-15 10:30:00
Runtime:            45.23 seconds

MAIN METRICS
--------------------------------------------------------------------------------
Metric                          Value
--------------------------------------------------------------------------------
Category Accuracy:              85.0%
Type Accuracy:                  95.0%
Amount Accuracy:                90.0%
Exact Match (All Correct):      78.0%

CLASSIFICATION METRICS (Macro-averaged)
--------------------------------------------------------------------------------
Macro Precision:                83.5%
Macro Recall:                   82.1%
Macro F1 Score:                 82.8%

PER-CATEGORY PERFORMANCE
--------------------------------------------------------------------------------
Category                 Precision      Recall      F1 Score   Support
--------------------------------------------------------------------------------
Cafe                         90.0%       85.0%       87.5%        10
Di chuyển                    88.0%       92.0%       90.0%        12
Giải trí                     85.0%       80.0%       82.5%         8
...
```

## API Endpoints

### POST /api/v1/predict

Dự đoán thông tin giao dịch từ mô tả tiếng Việt.

**Request:**

```json
{
  "text": "Mẹ cho 1tr",
  "categories": ["Quà tặng", "Lương", "Ăn uống", "Mượn tiền"],
  "locale": "vi-VN",
  "currency": "VND"
}
```

**Response:**

```json
{
  "amount": 1000000,
  "category": "Quà tặng",
  "type": "Thu nhập",
  "confidence": 0.88
}
```

### GET /api/v1/health

Kiểm tra trạng thái service và LLM availability.

```bash
curl http://localhost:8000/api/v1/health
```

### GET /api/v1/categories

Lấy danh sách danh mục mặc định.

```bash
curl http://localhost:8000/api/v1/categories
```

### POST /api/v1/predict/batch

Dự đoán hàng loạt cho nhiều giao dịch.

```bash
curl -X POST "http://localhost:8000/api/v1/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Cafe 30k", "Grab 50k", "Lương 10tr"]}'
```

## Danh mục được hỗ trợ

| Category | Ví dụ |
|----------|-------|
| 4G | Internet, Data, Wifi, tiền mạng |
| Cafe | Cafe, trà, sinh tố, đồ uống |
| Di chuyển | Xăng xe, taxi, bus, grab, xe ôm |
| Giáo dục | Học phí, sách vở, khóa học |
| Giải trí | Game, phim, du lịch, spotify |
| Hớt tóc | Cắt tóc, làm đầu, salon |
| Khác | Không khớp category nào |
| Mượn tiền | Vay tiền, mượn tiền |
| Mỹ phẩm chăm sóc da | Sữa tắm, xà bông, mỹ phẩm |
| Phiếu lương | Lương, thưởng, phụ cấp |
| Quà tặng | Quà tặng, được cho tiền |
| Sức khỏe | Thuốc, khám bệnh, y tế |
| Trả nợ | Trả nợ, thanh toán nợ |
| Tạp phẩm | Đồ dùng sinh hoạt, tạp hóa |
| Đám tiệc | Sinh nhật, đám cưới, tiệc |

## Cấu trúc dự án

```
KLTN_UIT_BE/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # Configuration loader
│   ├── routes/
│   │   ├── __init__.py
│   │   └── predict.py       # /predict endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py   # llama.cpp integration
│   │   ├── preprocessing.py # Text preprocessing
│   │   └── postprocessing.py # JSON parsing & validation
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── request_response.py # Pydantic models
│   └── prompts/
│       ├── __init__.py
│       └── system_prompts.py # Prompt templates
├── data/
│   ├── processed/
│   │   ├── training_data.json   # Dataset huấn luyện
│   │   ├── test_data.json       # Dataset test
│   │   └── category_mapping.json
│   └── evaluation/              # File sau khi chạy prepare_data.py
│       ├── aligned_train.csv
│       ├── aligned_test.csv
│       └── aligned_test_100.csv
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── test_llm_7b_direct.py    # Full evaluation script
├── quick_eval.py            # Quick test (30 cases)
├── prepare_data.py          # Data preparation
└── README.md
```

## Tích hợp với React Native

```javascript
// React Native code example
const predictTransaction = async (text, categories) => {
  try {
  const response = await fetch('http://<YOUR_IP>:8000/api/v1/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: text,
      categories: categories,
    }),
  });
  
  const data = await response.json();
  return {
    amount: data.amount,
    category: data.category,
    type: data.type,
    confidence: data.confidence,
  };
  } catch (error) {
    console.error('Prediction error:', error);
    return null;
  }
};

// Sử dụng
const result = await predictTransaction("Mẹ cho 1tr", ["Quà tặng", "Phiếu lương"]);
console.log(result);
// { amount: 1000000, category: "Quà tặng", type: "Thu nhập", confidence: 0.88 }
```

## Quy tắc số tiền

| Input | Output |
|-------|--------|
| "1tr", "1 triệu" | 1000000 VND |
| "500k", "500 nghìn" | 500000 VND |
| "50k" | 50000 VND |
| "10d", "10đ" | 10 VND |

## Hướng dẫn triển khai

### Bước 1 — Khởi động LLM Server

```bash
cd ../llama.cpp
./llama-server -m models/qwen2.5-7b-instruct-q4_k_m.gguf --port 8080 --host 127.0.0.1
```

### Bước 2 — Khởi động Backend

```bash
cd KLTN_UIT_BE
python -m app.main
```

### Bước 3 — Chạy Evaluation

```bash
# Chuẩn bị dữ liệu
python prepare_data.py

# Đánh giá model
python test_llm_7b_direct.py --file data/evaluation/aligned_test_100.csv
```

### Bước 4 — Tích hợp Frontend

Sử dụng API endpoints từ React Native app.

## Cải thiện độ chính xác

Nếu F1 Score < 80%, thử các phương pháp sau:

1. **Few-shot Learning**: Thêm ví dụ vào system prompt
2. **Category-specific prompts**: Tạo prompt riêng cho từng category khó
3. **Post-processing rules**: Thêm rules để sửa các lỗi thường gặp
4. **Fine-tuning**: Fine-tune Qwen2.5-7B với dataset của bạn (cần GPU mạnh)

## License

MIT License
