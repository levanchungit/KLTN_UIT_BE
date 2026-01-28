# KLTN_UIT_BE - AI Backend for Transaction Classification

FastAPI + llama.cpp Integration

## Mục tiêu

Xây dựng dịch vụ AI Backend nhận mô tả giao dịch tiếng Việt từ React Native, gọi LLM (Qwen/Gemma chạy bằng llama.cpp) để trích xuất số tiền + phân loại danh mục, trả về JSON:

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
React Native → POST /predict → FastAPI → llama.cpp /v1/chat/completions → JSON
```

## Cài đặt

### 1. Cài đặt dependencies

```bash
cd KLTN_UIT_BE
pip install -r requirements.txt
```

### 2. Cấu hình

Chỉnh sửa file `config.yaml` hoặc tạo file `.env`:

```bash
cp .env.example .env
```

Cấu hình LLM server:

```yaml
llm:
  base_url: "http://127.0.0.1:8080"  # llama.cpp server URL
  model: "qwen2.5-1.5b-instruct-q4_0.gguf"  # hoặc "gemma-2b-it-q4_0.gguf"
  temperature: 0.0
```

### 3. Khởi động LLM Server (llama.cpp)

```bash
# Tải llama.cpp Windows build
# Tải model GGUF (Qwen2.5-1.5B Instruct Q4 hoặc Gemma 2B Q4)

# Chạy llama-server
./llama-server -m qwen2.5-1.5b-instruct-q4_0.gguf --port 8080 --host 127.0.0.1
```

### 4. Khởi động FastAPI

```bash
# Development mode (với hot reload)
python -m app.main

# Hoặc
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### POST /api/v1/predict

Dự đoán thông tin giao dịch từ mô tả tiếng Việt.

**Request:**

```json
{
  "text": "Mẹ cho 1tr",
  "categories": ["Quà tặng", "Lương", "Ăn uống", "Mượn tiền", "Chuyển khoản"],
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

### GET /api/v1/categories

Lấy danh sách danh mục mặc định.

### POST /api/v1/predict/batch

Dự đoán hàng loạt cho nhiều giao dịch.

## Test

```bash
# Chạy tất cả tests
pytest tests/ -v

# Chạy tests cho preprocessing
pytest tests/test_preprocessing.py -v

# Chạy tests cho API
pytest tests/test_api.py -v
```

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
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   └── test_api.py
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md
```

## Danh mục mặc định

- Quà tặng
- Lương
- Ăn uống
- Mượn tiền
- Chuyển khoản
- Mua sắm
- Di chuyển
- Giải trí
- Sức khỏe
- Hóa đơn
- Giáo dục
- Khác

## Ví dụ sử dụng với cURL

```bash
# Test prediction
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Mẹ cho 1tr", "categories": ["Quà tặng", "Lương", "Ăn uống"]}'

# Health check
curl "http://localhost:8000/api/v1/health"

# Get categories
curl "http://localhost:8000/api/v1/categories"
```

## Tích hợp với React Native

```javascript
// React Native code example
const predictTransaction = async (text, categories) => {
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
};
```

## Hướng dẫn triển khai theo từng bước

### Bước 1 — Dựng LLM server

1. Tải llama.cpp (Windows build)
2. Tải model GGUF (Qwen2.5-1.5B Instruct Q4 hoặc Gemma 2B Q4)
3. Chạy llama-server trên 127.0.0.1:8080
4. Test gọi được endpoint /v1/chat/completions

### Bước 2 — Tạo FastAPI service

1. Tạo project Python, cài fastapi, uvicorn, requests
2. Tạo endpoint POST /predict nhận text + categories
3. Gọi llama.cpp qua HTTP theo format chat completion

### Bước 3 — Prompt Engineering (ép JSON)

1. Dùng system prompt quy định schema JSON + luật "category chỉ được chọn trong list"
2. User prompt gồm: Câu giao dịch + Danh sách category hợp lệ
3. Temperature = 0 để output ổn định

### Bước 4 — Tiền xử lý + Hậu xử lý

1. Tiền xử lý: chuẩn hoá text, quy đổi tiền 200k/1tr
2. Hậu xử lý: parse JSON, validate:
   - category phải thuộc categories[]
   - amount là số
   - type thuộc {Thu nhập, Chi tiêu, Chuyển khoản}
   - Tính/giới hạn confidence trong [0,1]
3. Nếu parse fail → trả lỗi kèm raw để debug

### Bước 5 — Tích hợp React Native

1. RN gọi POST /predict
2. Nhận JSON → render preview form (amount/category/type)
3. User confirm → app tạo giao dịch trong DB/local storage

### Bước 6 — Thử nghiệm & đánh giá

1. Chuẩn bị tập test (ví dụ 100–300 câu giao dịch)
2. Đánh giá:
   - Accuracy phân loại category
   - Accuracy trích xuất amount
   - Latency (thời gian phản hồi)
3. Ghi nhận trường hợp sai để chỉnh prompt/rule

## Tiêu chí hoàn thành (Deliverables)

- [ ] LLM server chạy ổn định (llama.cpp + model GGUF)
- [ ] FastAPI endpoint /predict trả JSON đúng schema
- [ ] React Native gọi được API và tạo giao dịch tự động
- [ ] Báo cáo kết quả thử nghiệm: accuracy + ví dụ đúng/sai + hướng cải thiện

## License

MIT License
