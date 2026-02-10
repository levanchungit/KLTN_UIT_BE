# 📊 BÁO CÁO SO SÁNH 3 MÔ HÌNH PHÂN LOẠI DANH MỤC

**Ngày tạo báo cáo:** 2026-02-10

---

## 📋 1. Tổng Quan Các Mô Hình

| # | Tên Mô Hình | Kích thước | Quantization |
|---|-------------|------------|--------------|
| 1 | **Gemma-2-9B-IT** | 9B tham số | Q4_K_M |
| 2 | **Qwen2.5-1.5B-Instruct** | 1.5B tham số | Q4_0 |
| 3 | **Qwen2.5-7B-Instruct** | 7B tham số | Q4_K_M |

---

## 📈 2. Bảng So Sánh Chỉ Số Tổng Hợp

| Chỉ số | Gemma-2-9B-IT | Qwen2.5-1.5B | Qwen2.5-7B | 🏆 Tốt nhất |
|--------|---------------|--------------|------------|-------------|
| **Tổng số mẫu input** | 510 | 510 | 510 | - |
| **Tổng giao dịch expected** | 716 | 716 | 716 | - |
| **Samples đúng hoàn toàn** | 471 (92.4%) | 400 (78.4%) | 474 (92.9%) | 🥇 Qwen2.5-7B |
| **Số mẫu lỗi** | 39 | 110 | 36 | 🥇 Qwen2.5-7B |
| **Thời gian phản hồi TB** | 58,543ms | 10,735ms | 37,943ms | 🥇 Qwen2.5-1.5B |
| **Macro Precision** | 88.6% | 83.5% | 86.3% | 🥇 Gemma-2-9B |
| **Macro Recall** | 84.7% | 74.0% | 84.2% | 🥇 Gemma-2-9B |
| **Macro F1 Score** | 86.6% | 77.8% | 85.2% | 🥇 Gemma-2-9B |

---

## 📊 3. Biểu Đồ So Sánh Hiệu Suất (Dạng Text)

### 3.1 Macro F1 Score
```
Gemma-2-9B-IT     ████████████████████████████████████████████ 86.6%
Qwen2.5-7B        ██████████████████████████████████████████   85.2%
Qwen2.5-1.5B      ████████████████████████████████████         77.8%
```

### 3.2 Samples Đúng Hoàn Toàn (%)
```
Qwen2.5-7B        ████████████████████████████████████████████ 92.9%
Gemma-2-9B-IT     ███████████████████████████████████████████  92.4%
Qwen2.5-1.5B      ██████████████████████████████████           78.4%
```

### 3.3 Thời Gian Phản Hồi (ms) - Thấp hơn là tốt hơn
```
Qwen2.5-1.5B      ████████                                     10,735ms
Qwen2.5-7B        ████████████████████████████                  37,943ms
Gemma-2-9B-IT     ████████████████████████████████████████████  58,543ms
```

---

## 📋 4. Metrics Chi Tiết Theo Danh Mục

### 4.1 Gemma-2-9B-IT-Q4_K_M

| Danh mục | Precision | Recall | F1 Score | Support | TP | FP | FN |
|----------|-----------|--------|----------|---------|----|----|-----|
| Ăn uống | 98.9% | 97.8% | 98.3% | 91 | 89 | 1 | 2 |
| Đi lại | 98.9% | 95.7% | 97.2% | 92 | 88 | 1 | 4 |
| Nhà ở | 100.0% | 90.8% | 95.2% | 87 | 79 | 0 | 8 |
| Mua sắm | 100.0% | 95.5% | 97.7% | 110 | 105 | 0 | 5 |
| Giải trí | 100.0% | 95.8% | 97.8% | 95 | 91 | 0 | 4 |
| Giáo dục | 100.0% | 98.7% | 99.3% | 76 | 75 | 0 | 1 |
| Y tế | 100.0% | 96.9% | 98.4% | 97 | 94 | 0 | 3 |
| Thu nhập | 100.0% | 91.2% | 95.4% | 68 | 62 | 0 | 6 |
| Chưa xác định | 0.0% | 0.0% | 0.0% | 0 | 0 | 35 | 0 |

### 4.2 Qwen2.5-1.5B-Instruct-Q4_0

| Danh mục | Precision | Recall | F1 Score | Support | TP | FP | FN |
|----------|-----------|--------|----------|---------|----|----|-----|
| Ăn uống | 87.8% | 86.8% | 87.3% | 91 | 79 | 11 | 12 |
| Đi lại | 100.0% | 85.9% | 92.4% | 92 | 79 | 0 | 13 |
| Nhà ở | 100.0% | 80.5% | 89.2% | 87 | 70 | 0 | 17 |
| Mua sắm | 100.0% | 73.6% | 84.8% | 110 | 81 | 0 | 29 |
| Giải trí | 100.0% | 78.9% | 88.2% | 95 | 75 | 0 | 20 |
| Giáo dục | 100.0% | 80.3% | 89.1% | 76 | 61 | 0 | 15 |
| Y tế | 100.0% | 90.7% | 95.1% | 97 | 88 | 0 | 9 |
| Thu nhập | 63.5% | 89.7% | 74.4% | 68 | 61 | 35 | 7 |
| Chưa xác định | 0.0% | 0.0% | 0.0% | 0 | 0 | 24 | 0 |

### 4.3 Qwen2.5-7B-Instruct-Q4_K_M

| Danh mục | Precision | Recall | F1 Score | Support | TP | FP | FN |
|----------|-----------|--------|----------|---------|----|----|-----|
| Ăn uống | 100.0% | 96.7% | 98.3% | 91 | 88 | 0 | 3 |
| Đi lại | 95.6% | 94.6% | 95.1% | 92 | 87 | 4 | 5 |
| Nhà ở | 100.0% | 90.8% | 95.2% | 87 | 79 | 0 | 8 |
| Mua sắm | 92.2% | 96.4% | 94.2% | 110 | 106 | 9 | 4 |
| Giải trí | 96.9% | 98.9% | 97.9% | 95 | 94 | 3 | 1 |
| Giáo dục | 100.0% | 92.1% | 95.9% | 76 | 70 | 0 | 6 |
| Y tế | 100.0% | 99.0% | 99.5% | 97 | 96 | 0 | 1 |
| Thu nhập | 92.4% | 89.7% | 91.0% | 68 | 61 | 5 | 7 |
| Chưa xác định | 0.0% | 0.0% | 0.0% | 0 | 0 | 13 | 0 |

---

## 📊 5. So Sánh F1 Score Theo Danh Mục

| Danh mục | Gemma-2-9B | Qwen2.5-1.5B | Qwen2.5-7B | 🏆 Tốt nhất |
|----------|------------|--------------|------------|-------------|
| **Ăn uống** | 98.3% | 87.3% | 98.3% | 🥇 Hòa (Gemma & Qwen-7B) |
| **Đi lại** | 97.2% | 92.4% | 95.1% | 🥇 Gemma |
| **Nhà ở** | 95.2% | 89.2% | 95.2% | 🥇 Hòa (Gemma & Qwen-7B) |
| **Mua sắm** | 97.7% | 84.8% | 94.2% | 🥇 Gemma |
| **Giải trí** | 97.8% | 88.2% | 97.9% | 🥇 Qwen-7B |
| **Giáo dục** | 99.3% | 89.1% | 95.9% | 🥇 Gemma |
| **Y tế** | 98.4% | 95.1% | 99.5% | 🥇 Qwen-7B |
| **Thu nhập** | 95.4% | 74.4% | 91.0% | 🥇 Gemma |
| **Chưa xác định** | 0.0% | 0.0% | 0.0% | - |

---

## 📊 6. So Sánh Recall Theo Danh Mục

| Danh mục | Gemma-2-9B | Qwen2.5-1.5B | Qwen2.5-7B | 🏆 Tốt nhất |
|----------|------------|--------------|------------|-------------|
| **Ăn uống** | 97.8% | 86.8% | 96.7% | 🥇 Gemma |
| **Đi lại** | 95.7% | 85.9% | 94.6% | 🥇 Gemma |
| **Nhà ở** | 90.8% | 80.5% | 90.8% | 🥇 Hòa (Gemma & Qwen-7B) |
| **Mua sắm** | 95.5% | 73.6% | 96.4% | 🥇 Qwen-7B |
| **Giải trí** | 95.8% | 78.9% | 98.9% | 🥇 Qwen-7B |
| **Giáo dục** | 98.7% | 80.3% | 92.1% | 🥇 Gemma |
| **Y tế** | 96.9% | 90.7% | 99.0% | 🥇 Qwen-7B |
| **Thu nhập** | 91.2% | 89.7% | 89.7% | 🥇 Gemma |

---

## 📊 7. So Sánh Precision Theo Danh Mục

| Danh mục | Gemma-2-9B | Qwen2.5-1.5B | Qwen2.5-7B | 🏆 Tốt nhất |
|----------|------------|--------------|------------|-------------|
| **Ăn uống** | 98.9% | 87.8% | 100.0% | 🥇 Qwen-7B |
| **Đi lại** | 98.9% | 100.0% | 95.6% | 🥇 Qwen-1.5B |
| **Nhà ở** | 100.0% | 100.0% | 100.0% | 🥇 Hòa |
| **Mua sắm** | 100.0% | 100.0% | 92.2% | 🥇 Hòa (Gemma & Qwen-1.5B) |
| **Giải trí** | 100.0% | 100.0% | 96.9% | 🥇 Hòa (Gemma & Qwen-1.5B) |
| **Giáo dục** | 100.0% | 100.0% | 100.0% | 🥇 Hòa |
| **Y tế** | 100.0% | 100.0% | 100.0% | 🥇 Hòa |
| **Thu nhập** | 100.0% | 63.5% | 92.4% | 🥇 Gemma |

---

## 🔍 8. Phân Tích Ưu/Nhược Điểm

### 8.1 Gemma-2-9B-IT-Q4_K_M

| ✅ Ưu điểm | ❌ Nhược điểm |
|------------|--------------|
| Macro F1 Score cao nhất (86.6%) | Thời gian phản hồi chậm nhất (58.5s) |
| Precision rất cao, đa số 100% | Không xử lý tốt danh mục "Chưa xác định" (FP: 35) |
| Recall cân bằng tốt trên mọi danh mục | Yêu cầu tài nguyên tính toán lớn nhất |
| Giáo dục đạt F1 99.3% cao nhất | Chậm gấp ~5.5 lần so với Qwen2.5-1.5B |

### 8.2 Qwen2.5-1.5B-Instruct-Q4_0

| ✅ Ưu điểm | ❌ Nhược điểm |
|------------|--------------|
| Thời gian phản hồi nhanh nhất (10.7s) | F1 Score thấp nhất (77.8%) |
| Nhẹ, phù hợp với thiết bị hạn chế | Recall thấp ở nhiều danh mục (Mua sắm: 73.6%) |
| Precision 100% ở nhiều danh mục | Hay nhầm lẫn với danh mục "Thu nhập" (FP: 35) |
| Model nhỏ nhất (1.5B tham số) | Bỏ sót nhiều giao dịch (110 mẫu lỗi) |

### 8.3 Qwen2.5-7B-Instruct-Q4_K_M

| ✅ Ưu điểm | ❌ Nhược điểm |
|------------|--------------|
| Samples đúng hoàn toàn cao nhất (92.9%) | Thời gian phản hồi trung bình (37.9s) |
| Ít mẫu lỗi nhất (36 mẫu) | Precision Mua sắm thấp hơn (92.2%) |
| Y tế đạt F1 99.5% - cao nhất trong tất cả | FP ở Mua sắm cao (9) |
| Giải trí Recall cao nhất (98.9%) | Macro F1 thấp hơn Gemma nhẹ (-1.4%) |
| Cân bằng tốt giữa Precision & Recall | - |

---

## 📌 9. Kết Luận và Đề Xuất

### 9.1 Xếp Hạng Tổng Thể

| Hạng | Mô Hình | Macro F1 | Samples đúng | Mẫu lỗi | Thời gian |
|------|---------|----------|--------------|----------|-----------|
| 🥇 1 | **Gemma-2-9B-IT** | 86.6% | 92.4% | 39 | 58.5s |
| 🥈 2 | **Qwen2.5-7B** | 85.2% | **92.9%** | **36** | 37.9s |
| 🥉 3 | **Qwen2.5-1.5B** | 77.8% | 78.4% | 110 | **10.7s** |

### 9.2 Đề Xuất Theo Trường Hợp Sử Dụng

| Trường hợp | Mô hình đề xuất | Lý do |
|------------|-----------------|-------|
| **Ưu tiên Macro F1 cao nhất** | Gemma-2-9B-IT | F1 Score cao nhất (86.6%) |
| **Ưu tiên ít lỗi nhất trên toàn bộ mẫu** | Qwen2.5-7B | Ít mẫu lỗi nhất (36), Samples đúng cao nhất (92.9%) |
| **Ưu tiên tốc độ** | Qwen2.5-1.5B | Thời gian phản hồi nhanh nhất (10.7s) |
| **Cân bằng tốc độ & chính xác** | Qwen2.5-7B | F1 tốt (85.2%), nhanh hơn Gemma ~35% |
| **Thiết bị tài nguyên hạn chế** | Qwen2.5-1.5B | Model nhẹ nhất (1.5B tham số) |
| **Ứng dụng production** | Qwen2.5-7B hoặc Gemma-2-9B-IT | Độ tin cậy cao, ít lỗi |

### 9.3 Nhận Xét Chung

1. **Gemma-2-9B-IT** vẫn dẫn đầu về Macro F1 Score (86.6%), nhưng chậm nhất với thời gian phản hồi 58.5 giây/mẫu. Precision gần như hoàn hảo (100% ở 6/8 danh mục).

2. **Qwen2.5-7B** là bất ngờ lớn nhất - đạt tỷ lệ samples đúng hoàn toàn cao nhất (92.9%) và ít mẫu lỗi nhất (36), vượt Gemma-2-9B dù Macro F1 thấp hơn nhẹ. Đặc biệt mạnh ở Y tế (F1: 99.5%) và Giải trí (F1: 97.9%). Thời gian phản hồi nhanh hơn Gemma ~35%.

3. **Qwen2.5-1.5B** phù hợp cho các ứng dụng yêu cầu phản hồi nhanh hoặc chạy trên thiết bị có tài nguyên hạn chế, nhưng cần chấp nhận độ chính xác thấp hơn đáng kể (78.4% vs 92.9%).

4. **Điểm yếu chung**: Cả 3 mô hình đều có vấn đề với danh mục "Chưa xác định" (F1 = 0%), tức là hay dự đoán thêm giao dịch "Chưa xác định" mà không cần thiết.

---

## 📎 10. Thông Tin Bổ Sung

### Thời gian đánh giá
- Gemma-2-9B-IT: 2026-02-08T10:26:11.828Z
- Qwen2.5-1.5B: 2026-02-07T06:38:14.749Z
- Qwen2.5-7B: 2026-02-09T17:21:35.955Z

### Ghi chú
- Tất cả các mô hình đều được quantize để tối ưu hóa bộ nhớ và tốc độ
- Dữ liệu test là 510 câu nhập liệu chi tiêu/thu nhập bằng tiếng Việt tự nhiên, tổng cộng 716 giao dịch expected
- Các danh mục phân loại: Ăn uống, Đi lại, Nhà ở, Mua sắm, Giải trí, Giáo dục, Y tế, Thu nhập, Chưa xác định

---

*Báo cáo được tạo tự động từ dữ liệu đánh giá mô hình AI - Cập nhật lần cuối: 2026-02-10*
