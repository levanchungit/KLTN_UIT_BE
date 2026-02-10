# 📊 Báo Cáo Đánh Giá Mô Hình AI

---

## 📋 Thông Tin Chung

| Thông tin | Giá trị |
|-----------|--------|
| **Thời gian đánh giá** | 2026-02-08T10:26:11.828Z |
| **Tổng số mẫu input** | 510 |
| **Tổng số giao dịch expected** | 716 |
| **Samples đúng hoàn toàn** | 471 (92.4%) |
| **Thời gian phản hồi TB** | 58543ms |

---

## 📈 Bảng 1: Tổng Hợp Metrics

| Metric | Giá trị |
|--------|--------|
| **Macro Precision** | 88.6% |
| **Macro Recall** | 84.7% |
| **Macro F1 Score** | 86.6% |

---

## 📊 Bảng 2: Metrics Theo Danh Mục

| Danh mục | Precision | Recall | F1 Score | Support | TP | FP | FN |
|----------|-----------|--------|----------|---------|----|----|----|
| Ăn uống | 98.9% | 97.8% | 98.3% | 91 | 89 | 1 | 2 |
| Đi lại | 98.9% | 95.7% | 97.2% | 92 | 88 | 1 | 4 |
| Nhà ở | 100.0% | 90.8% | 95.2% | 87 | 79 | 0 | 8 |
| Mua sắm | 100.0% | 95.5% | 97.7% | 110 | 105 | 0 | 5 |
| Giải trí | 100.0% | 95.8% | 97.8% | 95 | 91 | 0 | 4 |
| Giáo dục | 100.0% | 98.7% | 99.3% | 76 | 75 | 0 | 1 |
| Y tế | 100.0% | 96.9% | 98.4% | 97 | 94 | 0 | 3 |
| Thu nhập | 100.0% | 91.2% | 95.4% | 68 | 62 | 0 | 6 |
| Chưa xác định | 0.0% | 0.0% | 0.0% | 0 | 0 | 35 | 0 |

---

## 📝 Bảng 3: Chi Tiết Từng Mẫu Đánh Giá

**Chú thích:** ✅ = Đúng (TP) | ❌ = Bỏ sót (FN) | ⚠️ = Dư thừa (FP)

**Tổng kết:** ✅ Đúng hoàn toàn: 471 | ❌ Có lỗi: 39

| # | Input Text | Expected | Predicted | Status | Chi tiết |
|---|------------|----------|-----------|--------|----------|
| 1 | di rua xe het 1930k cộng 330 cành bus | Đi lại (1.9tr)<br>Đi lại (330k) | Chưa xác định (1.9tr)<br>Đi lại (330k) | ❌ | ✅ Đi lại<br>❌ Missed: Đi lại<br>⚠️ Extra: Chưa xác định |
| 2 | đi áo thun hết 1080k, đi karaoke hết 2530k thêm... | Mua sắm (1.1tr)<br>Giải trí (2.5tr)<br>Giải trí (3.3tr) | Mua sắm (1.1tr)<br>Giải trí (2.5tr)<br>Mua sắm (3.3tr) | ✅ | ✅ Mua sắm<br>✅ Giải trí<br>✅ Giải trí |
| 3 | mới bóng đèn 3.94 triệu | Nhà ở (3.9tr) | Mua sắm (3.9tr) | ✅ | ✅ Nhà ở |
| 4 | đóng thực phẩm 860 ngàn | Mua sắm (860k) | Ăn uống (860k) | ✅ | ✅ Mua sắm |
| 5 | kính thuốc 1450000 | Y tế (1.4tr) | Y tế (1.4tr) | ✅ | ✅ Y tế |
| 6 | sách 590.000 thêm di tap chi het 2190 ngan | Mua sắm (590k)<br>Mua sắm (2.2tr) | Mua sắm (590k)<br>Chưa xác định (2.2tr) | ✅ | ✅ Mua sắm<br>✅ Mua sắm |
| 7 | 9470 canh hoan tien | Thu nhập (9.5tr) | Chưa xác định (9k) | ❌ | ❌ Missed: Thu nhập<br>⚠️ Extra: Chưa xác định |
| 8 | đi tiền nhà hết 1560 cành | Nhà ở (1.6tr) | Chưa xác định (1.6tr) | ✅ | ✅ Nhà ở |
| 9 | đóng cơm tấm 480.000 | Ăn uống (480k) | Ăn uống (480k) | ✅ | ✅ Ăn uống |
| 10 | photo tài liệu 9.64 triệu | Giáo dục (9.6tr) | Chưa xác định (9.6tr) | ✅ | ✅ Giáo dục |
| 11 | lì xì 5490k thêm 890 ngàn vé máy bay | Thu nhập (5.5tr)<br>Đi lại (890k) | Chưa xác định (5.5tr)<br>Chưa xác định (890k)<br>Chưa xác định (0đ) | ❌ | ✅ Thu nhập<br>✅ Đi lại<br>⚠️ Extra: Chưa xác định |
| 12 | netflix 2280k | Giải trí (2.3tr) | Giải trí (2.3tr) | ✅ | ✅ Giải trí |
| 13 | đóng taxi 1.92 triệu | Đi lại (1.9tr) | Đi lại (1.9tr) | ✅ | ✅ Đi lại |
| 14 | 1620 cành điện | Nhà ở (1.6tr) | Chưa xác định (0đ) | ❌ | ❌ Missed: Nhà ở<br>⚠️ Extra: Chưa xác định |
| 15 | thu tap chi 2.01m | Mua sắm (2.0tr) | Thu nhập (2.0tr) | ✅ | ✅ Mua sắm |
| 16 | đi lì xì hết 10640 cành với đi khám bệnh hết 79... | Thu nhập (10.6tr)<br>Y tế (790k) | Chưa xác định (11k)<br>Y tế (790k) | ❌ | ❌ Missed: Thu nhập<br>✅ Y tế<br>⚠️ Extra: Chưa xác định |
| 17 | phở 250k | Ăn uống (250k) | Ăn uống (250k) | ✅ | ✅ Ăn uống |
| 18 | 3650 ngàn bowling, 310000 vé xe | Giải trí (3.6tr)<br>Đi lại (310k) | Giải trí (3.6tr)<br>Đi lại (310k) | ✅ | ✅ Giải trí<br>✅ Đi lại |
| 19 | 220.000 ielts | Giáo dục (220k) | Giáo dục (220k) | ✅ | ✅ Giáo dục |
| 20 | thu bun bo 65000 rồi đi đi chợ hết 510k | Ăn uống (65k)<br>Mua sắm (510k) | Ăn uống (65k)<br>Mua sắm (510k) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 21 | 16.84tr thưởng | Thu nhập (16.8tr) | Thu nhập (16.8tr) | ✅ | ✅ Thu nhập |
| 22 | váy 1440 ngàn | Mua sắm (1.4tr) | Mua sắm (1.4tr) | ✅ | ✅ Mua sắm |
| 23 | 3.720.000 ielts | Giáo dục (3.7tr) | Giáo dục (3.7tr) | ✅ | ✅ Giáo dục |
| 24 | 3300000 tiền điện với mới viện phí 820 ngàn | Nhà ở (3.3tr)<br>Y tế (820k) | Nhà ở (3.3tr)<br>Y tế (820k) | ✅ | ✅ Nhà ở<br>✅ Y tế |
| 25 | 990 canh tien vien phi, được lương 19160 ngàn | Y tế (990k)<br>Thu nhập (19.2tr) | Chưa xác định (990k)<br>Thu nhập (19.2tr) | ✅ | ✅ Y tế<br>✅ Thu nhập |
| 26 | cơm tấm 220 cành | Ăn uống (220k) | Ăn uống (220k) | ✅ | ✅ Ăn uống |
| 27 | thu tra sua 400.000 thêm thanh toán thuốc 1730000 | Ăn uống (400k)<br>Y tế (1.7tr) | Ăn uống (400k)<br>Y tế (1.7tr) | ✅ | ✅ Ăn uống<br>✅ Y tế |
| 28 | đi nhổ răng hết 1010 cành. đi hủ tiếu hết 430 ngàn | Y tế (1.0tr)<br>Ăn uống (430k) | Y tế (1.0tr)<br>Ăn uống (430k) | ✅ | ✅ Y tế<br>✅ Ăn uống |
| 29 | đi bút hết 6.44m thêm chi xét nghiệm 130 ngàn | Giáo dục (6.4tr)<br>Y tế (130k) | Chưa xác định (6.4tr)<br>Y tế (130k) | ✅ | ✅ Giáo dục<br>✅ Y tế |
| 30 | đi đổ xăng hết 850 cành | Đi lại (850k) | Đi lại (850k) | ✅ | ✅ Đi lại |
| 31 | 270000 rau củ | Mua sắm (270k) | Mua sắm (270k) | ✅ | ✅ Mua sắm |
| 32 | có thưởng 1.2 triệu lúc nãy | Thu nhập (1.2tr) | Thu nhập (1.2tr) | ✅ | ✅ Thu nhập |
| 33 | toeic 3330000 | Giáo dục (3.3tr) | Giáo dục (3.3tr) | ✅ | ✅ Giáo dục |
| 34 | rau củ 940000 | Mua sắm (940k) | Ăn uống (940k) | ✅ | ✅ Mua sắm |
| 35 | vé máy bay 650k với chi sửa xe 940k lúc nãy | Đi lại (650k)<br>Đi lại (940k) | Chưa xác định (650k)<br>Nhà ở (940k) | ✅ | ✅ Đi lại<br>✅ Đi lại |
| 36 | 1290 cành tiền dịch vụ chung cư | Nhà ở (1.3tr) | Nhà ở (1.3tr) | ✅ | ✅ Nhà ở |
| 37 | lương thưởng 3280k | Thu nhập (3.3tr) | Thu nhập (3.3tr)<br>Chưa xác định (0đ) | ❌ | ✅ Thu nhập<br>⚠️ Extra: Chưa xác định |
| 38 | đi quần áo hết 1910 ngàn, 200000 tiền bảo dưỡng xe | Mua sắm (1.9tr)<br>Đi lại (200k) | Mua sắm (1.9tr)<br>Đi lại (200k) | ✅ | ✅ Mua sắm<br>✅ Đi lại |
| 39 | 2300k tiền siêu thị | Mua sắm (2.3tr) | Mua sắm (2.3tr) | ✅ | ✅ Mua sắm |
| 40 | đi vé máy bay hết 1490k | Đi lại (1.5tr) | Đi lại (1.5tr) | ✅ | ✅ Đi lại |
| 41 | 2.33 triệu tiền giày | Mua sắm (2.3tr) | Mua sắm (2.3tr) | ✅ | ✅ Mua sắm |
| 42 | be 280000 sau đó moi cf 50k chieu nay | Đi lại (280k)<br>Ăn uống (50k) | Chưa xác định (280k)<br>Ăn uống (50k) | ✅ | ✅ Đi lại<br>✅ Ăn uống |
| 43 | đi nước muối hết 210000 | Y tế (210k) | Y tế (210k) | ✅ | ✅ Y tế |
| 44 | 970.000 tiền thực phẩm | Mua sắm (970k) | Ăn uống (970k) | ✅ | ✅ Mua sắm |
| 45 | 14.62tr bán đồ cũ. đi xét nghiệm hết 250.000 | Thu nhập (14.6tr)<br>Y tế (250k) | Thu nhập (14.6tr)<br>Y tế (250k) | ✅ | ✅ Thu nhập<br>✅ Y tế |
| 46 | chi khám bệnh 1.33 triệu hôm kia | Y tế (1.3tr) | Y tế (1.3tr) | ✅ | ✅ Y tế |
| 47 | kính thuốc 1.11m sau đó thanh toán ielts 6190 n... | Y tế (1.1tr)<br>Giáo dục (6.2tr)<br>Đi lại (1.8tr) | Y tế (1.1tr)<br>Giáo dục (6.2tr)<br>Đi lại (1.8tr) | ✅ | ✅ Y tế<br>✅ Giáo dục<br>✅ Đi lại |
| 48 | đi vé xem phim hết 95k | Giải trí (95k) | Giải trí (95k) | ✅ | ✅ Giải trí |
| 49 | game 2630 ngàn sau đó đi gojek hết 600 cành | Giải trí (2.6tr)<br>Đi lại (600k) | Giải trí (2.6tr)<br>Đi lại (600k) | ✅ | ✅ Giải trí<br>✅ Đi lại |
| 50 | di wifi het 1590 canh | Nhà ở (1.6tr) | Chưa xác định (1.6tr) | ✅ | ✅ Nhà ở |
| 51 | đi karaoke hết 1740 cành | Giải trí (1.7tr) | Giải trí (1.7tr) | ✅ | ✅ Giải trí |
| 52 | thanh toán vé xem phim 4940000 chiều nay | Giải trí (4.9tr) | Giải trí (4.9tr) | ✅ | ✅ Giải trí |
| 53 | đi bóng đèn hết 1.430.000 | Nhà ở (1.4tr) | Mua sắm (1.4tr) | ✅ | ✅ Nhà ở |
| 54 | lì xì 1.770.000 | Thu nhập (1.8tr) | Thu nhập (1.8tr) | ✅ | ✅ Thu nhập |
| 55 | du lịch 4060k | Giải trí (4.1tr) | Giải trí (4.1tr) | ✅ | ✅ Giải trí |
| 56 | 2020000 đòi nợ | Thu nhập (2.0tr) | Chưa xác định (2.0tr) | ❌ | ❌ Missed: Thu nhập<br>⚠️ Extra: Chưa xác định |
| 57 | đi quần áo hết 1420k - váy 810 cành | Mua sắm (1.4tr)<br>Mua sắm (810k) | Mua sắm (1.4tr)<br>Mua sắm (810k) | ✅ | ✅ Mua sắm<br>✅ Mua sắm |
| 58 | 2770 ngàn đi chợ | Mua sắm (2.8tr) | Mua sắm (2.8tr) | ✅ | ✅ Mua sắm |
| 59 | đi nhậu hết 100.000 | Ăn uống (100k) | Ăn uống (100k) | ✅ | ✅ Ăn uống |
| 60 | hoàn tiền 9.19m | Thu nhập (9.2tr) | Thu nhập (9.2tr) | ✅ | ✅ Thu nhập |
| 61 | netflix 470.000, nhậu 35 cành với 480 ngàn tiền be | Giải trí (470k)<br>Ăn uống (35k)<br>Đi lại (480k) | Giải trí (470k)<br>Ăn uống (480k) | ❌ | ✅ Giải trí<br>✅ Ăn uống<br>❌ Missed: Đi lại |
| 62 | chi sửa xe 390 ngàn | Đi lại (390k) | Chưa xác định (390k) | ✅ | ✅ Đi lại |
| 63 | đóng sửa xe 1270 ngàn | Đi lại (1.3tr) | Chưa xác định (1.3tr) | ✅ | ✅ Đi lại |
| 64 | đóng rác 2.35 triệu. wifi 1630k | Nhà ở (2.4tr)<br>Nhà ở (1.6tr) | Chưa xác định (2.4tr)<br>Chưa xác định (1.6tr) | ✅ | ✅ Nhà ở<br>✅ Nhà ở |
| 65 | đi gojek hết 1020 cành | Đi lại (1.0tr) | Đi lại (1.0tr) | ✅ | ✅ Đi lại |
| 66 | 300.000 xăng | Đi lại (300k) | Đi lại (300k) | ✅ | ✅ Đi lại |
| 67 | rau củ 2.830.000 | Mua sắm (2.8tr) | Mua sắm (2.8tr) | ✅ | ✅ Mua sắm |
| 68 | thu game 1.130.000 | Giải trí (1.1tr) | Giải trí (1.1tr) | ✅ | ✅ Giải trí |
| 69 | sách giáo khoa 950.000 | Giáo dục (950k) | Giáo dục (950k) | ✅ | ✅ Giáo dục |
| 70 | túi xách 2.960.000 | Mua sắm (3.0tr) | Mua sắm (3.0tr) | ✅ | ✅ Mua sắm |
| 71 | di dien het 2920k | Nhà ở (2.9tr) | Chưa xác định (2.9tr) | ✅ | ✅ Nhà ở |
| 72 | 510000 tiền thuốc | Y tế (510k) | Y tế (510k) | ✅ | ✅ Y tế |
| 73 | 700 ngàn tiền bảo hiểm y tế | Y tế (700k) | Y tế (700k) | ✅ | ✅ Y tế |
| 74 | 3.77 triệu toeic | Giáo dục (3.8tr) | Giáo dục (3.8tr) | ✅ | ✅ Giáo dục |
| 75 | bảo dưỡng xe 1920k | Đi lại (1.9tr) | Chưa xác định (1.9tr) | ✅ | ✅ Đi lại |
| 76 | 9.29 triệu tiền vở | Giáo dục (9.3tr) | Giáo dục (9.3tr) | ✅ | ✅ Giáo dục |
| 77 | đi karaoke hết 1560k | Giải trí (1.6tr) | Giải trí (1.6tr) | ✅ | ✅ Giải trí |
| 78 | sữa tắm 2.25m | Mua sắm (2.3tr) | Mua sắm (2.3tr) | ✅ | ✅ Mua sắm |
| 79 | dong my pham 240k chieu nay và mỹ phẩm 2000 càn... | Mua sắm (240k)<br>Mua sắm (2.0tr)<br>Đi lại (1.4tr) | Chưa xác định (240k)<br>Mua sắm (2k)<br>Nhà ở (1.4tr) | ❌ | ✅ Mua sắm<br>❌ Missed: Mua sắm<br>✅ Đi lại<br>⚠️ Extra: Chưa xác định |
| 80 | bút 890 ngàn | Giáo dục (890k) | Mua sắm (890k) | ✅ | ✅ Giáo dục |
| 81 | đi karaoke hết 680.000 | Giải trí (680k) | Giải trí (680k) | ✅ | ✅ Giải trí |
| 82 | đi tiền học hết 160.000 | Giáo dục (160k) | Giáo dục (160k) | ✅ | ✅ Giáo dục |
| 83 | đi xét nghiệm hết 300000 | Y tế (300k) | Y tế (300k) | ✅ | ✅ Y tế |
| 84 | trả cafe 80k. thanh toán du lịch 2330 ngàn lúc ... | Ăn uống (80k)<br>Giải trí (2.3tr)<br>Đi lại (220k) | Ăn uống (80k)<br>Chưa xác định (2.3tr)<br>Đi lại (220k) | ✅ | ✅ Ăn uống<br>✅ Giải trí<br>✅ Đi lại |
| 85 | 1.47 trieu bao hiem y te | Y tế (1.5tr) | Y tế (1.5tr) | ✅ | ✅ Y tế |
| 86 | thanh toán nước muối 1740 ngàn - 2.610.000 tiền... | Y tế (1.7tr)<br>Mua sắm (2.6tr) | Chưa xác định (1.7tr)<br>Mua sắm (2.6tr) | ✅ | ✅ Y tế<br>✅ Mua sắm |
| 87 | netflix 4100k | Giải trí (4.1tr) | Giải trí (4.1tr) | ✅ | ✅ Giải trí |
| 88 | xăng 1480k | Đi lại (1.5tr) | Đi lại (1.5tr) | ✅ | ✅ Đi lại |
| 89 | tiền trọ 2260000 cộng đi túi xách hết 1.38tr | Nhà ở (2.3tr)<br>Mua sắm (1.4tr) | Nhà ở (2.3tr)<br>Mua sắm (1.4tr) | ✅ | ✅ Nhà ở<br>✅ Mua sắm |
| 90 | sách giáo khoa 390.000 | Giáo dục (390k) | Giáo dục (390k) | ✅ | ✅ Giáo dục |
| 91 | đi cơm tấm hết 500000 | Ăn uống (500k) | Ăn uống (500k) | ✅ | ✅ Ăn uống |
| 92 | đi taxi hết 370.000 | Đi lại (370k) | Đi lại (370k) | ✅ | ✅ Đi lại |
| 93 | viện phí 1.35 triệu | Y tế (1.4tr) | Y tế (1.4tr) | ✅ | ✅ Y tế |
| 94 | nhận hoàn tiền 1.980.000 rồi xem phim 2210 ngàn... | Thu nhập (2.0tr)<br>Giải trí (2.2tr)<br>Nhà ở (1.2tr) | Thu nhập (2.0tr)<br>Giải trí (2.2tr)<br>Nhà ở (1.2tr) | ✅ | ✅ Thu nhập<br>✅ Giải trí<br>✅ Nhà ở |
| 95 | mới khóa học online 7.45m | Giáo dục (7.5tr) | Giáo dục (7.5tr) | ✅ | ✅ Giáo dục |
| 96 | đi bus hết 820 cành | Đi lại (820k) | Đi lại (820k) | ✅ | ✅ Đi lại |
| 97 | lì xì 15160 ngàn - nhậu 190 ngàn | Thu nhập (15.2tr)<br>Ăn uống (190k) | Thu nhập (15.2tr)<br>Ăn uống (190k) | ✅ | ✅ Thu nhập<br>✅ Ăn uống |
| 98 | đi chợ 1.010.000 - sách giáo khoa 5570k | Mua sắm (1.0tr)<br>Giáo dục (5.6tr) | Chưa xác định (1.0tr)<br>Giáo dục (5.6tr) | ✅ | ✅ Mua sắm<br>✅ Giáo dục |
| 99 | sinh tố 490k | Ăn uống (490k) | Ăn uống (490k) | ✅ | ✅ Ăn uống |
| 100 | nước muối 1.79tr | Y tế (1.8tr) | Chưa xác định (1.8tr) | ✅ | ✅ Y tế |
| 101 | sách giáo khoa 2.53tr. di karaoke het 3.38 trie... | Giáo dục (2.5tr)<br>Giải trí (3.4tr)<br>Giải trí (690k) | Giáo dục (2.5tr)<br>Giải trí (3.4tr)<br>Giải trí (690k) | ✅ | ✅ Giáo dục<br>✅ Giải trí<br>✅ Giải trí |
| 102 | đi nhổ răng hết 1.87 triệu | Y tế (1.9tr) | Y tế (1.9tr) | ✅ | ✅ Y tế |
| 103 | bus 1220 ngàn | Đi lại (1.2tr) | Đi lại (1.2tr) | ✅ | ✅ Đi lại |
| 104 | bảo dưỡng xe 580 cành rồi bảo hiểm y tế 1.710.0... | Đi lại (580k)<br>Y tế (1.7tr)<br>Mua sắm (2.0tr) | Chưa xác định (580k)<br>Y tế (1.7tr)<br>Ăn uống (2.0tr) | ✅ | ✅ Đi lại<br>✅ Y tế<br>✅ Mua sắm |
| 105 | di internet het 3600 ngan và đi chợ 680.000 | Nhà ở (3.6tr)<br>Mua sắm (680k) | Chưa xác định (360k)<br>Mua sắm (680k) | ❌ | ❌ Missed: Nhà ở<br>✅ Mua sắm<br>⚠️ Extra: Chưa xác định |
| 106 | 4440000 vở | Giáo dục (4.4tr) | Chưa xác định (4.4tr) | ✅ | ✅ Giáo dục |
| 107 | đi bia hết 400.000 - sách giáo khoa 990 ngàn | Ăn uống (400k)<br>Giáo dục (990k) | Ăn uống (400k)<br>Giáo dục (990k) | ✅ | ✅ Ăn uống<br>✅ Giáo dục |
| 108 | đi vở hết 3.98tr và khám bệnh 510 cành | Giáo dục (4.0tr)<br>Y tế (510k) | Mua sắm (4.0tr)<br>Y tế (510k) | ✅ | ✅ Giáo dục<br>✅ Y tế |
| 109 | chi rau cu 1160 ngan rồi đi khóa học online hết... | Mua sắm (1.2tr)<br>Giáo dục (9.2tr) | Ăn uống (1.2tr)<br>Giáo dục (9.2tr) | ✅ | ✅ Mua sắm<br>✅ Giáo dục |
| 110 | nhận túi xách 240 cành | Mua sắm (240k) | Chưa xác định (2.4tr) | ❌ | ❌ Missed: Mua sắm<br>⚠️ Extra: Chưa xác định |
| 111 | áo thun 970.000 | Mua sắm (970k) | Mua sắm (970k) | ✅ | ✅ Mua sắm |
| 112 | di tra sua het 430k. 3.620.000 lãi ngân hàng | Ăn uống (430k)<br>Thu nhập (3.6tr) | Chưa xác định (430k)<br>Thu nhập (3.6tr) | ✅ | ✅ Ăn uống<br>✅ Thu nhập |
| 113 | nước muối 710000 rồi 45 cành cà phê | Y tế (710k)<br>Ăn uống (45k) | Chưa xác định (710k)<br>Chưa xác định (0đ) | ❌ | ✅ Y tế<br>❌ Missed: Ăn uống<br>⚠️ Extra: Chưa xác định |
| 114 | di dung cu hoc tap het 6860000 | Giáo dục (6.9tr) | Giáo dục (6.9tr) | ✅ | ✅ Giáo dục |
| 115 | đi vé xem phim hết 580.000 | Giải trí (580k) | Giải trí (580k) | ✅ | ✅ Giải trí |
| 116 | đi gà rán hết 290 ngàn với 1320k tiền nước muối | Ăn uống (290k)<br>Y tế (1.3tr) | Ăn uống (290k)<br>Chưa xác định (1.3tr) | ✅ | ✅ Ăn uống<br>✅ Y tế |
| 117 | đóng gojek 680000 sau đó đi cơm tấm hết 450k vớ... | Đi lại (680k)<br>Ăn uống (450k)<br>Giải trí (4.5tr) | Đi lại (680k)<br>Ăn uống (450k)<br>Giải trí (4.5tr) | ✅ | ✅ Đi lại<br>✅ Ăn uống<br>✅ Giải trí |
| 118 | đi vở hết 4270 ngàn thêm tiền công 8490 cành | Giáo dục (4.3tr)<br>Thu nhập (8.5tr) | Chưa xác định (4.3tr)<br>Thu nhập (8.5tr) | ✅ | ✅ Giáo dục<br>✅ Thu nhập |
| 119 | du lịch 3890 cành | Giải trí (3.9tr) | Chưa xác định (4k) | ❌ | ❌ Missed: Giải trí<br>⚠️ Extra: Chưa xác định |
| 120 | đi pizza hết 490k | Ăn uống (490k) | Ăn uống (490k) | ✅ | ✅ Ăn uống |
| 121 | vừa tiền trọ 4.45 triệu | Nhà ở (4.5tr) | Nhà ở (4.5tr) | ✅ | ✅ Nhà ở |
| 122 | 480 ngàn tiền gà rán | Ăn uống (480k) | Ăn uống (480k) | ✅ | ✅ Ăn uống |
| 123 | netflix 3860 ngàn | Giải trí (3.9tr) | Giải trí (3.9tr) | ✅ | ✅ Giải trí |
| 124 | 180 cành tiền bún bò | Ăn uống (180k) | Ăn uống (180k) | ✅ | ✅ Ăn uống |
| 125 | 730 cành kính thuốc | Y tế (730k) | Chưa xác định (7.3tr)<br>Y tế (100k) | ❌ | ✅ Y tế<br>⚠️ Extra: Chưa xác định |
| 126 | điện 1.34tr | Nhà ở (1.3tr) | Chưa xác định (1.3tr) | ✅ | ✅ Nhà ở |
| 127 | di bowling het 160.000 | Giải trí (160k) | Giải trí (160k) | ✅ | ✅ Giải trí |
| 128 | 2370000 karaoke, rửa xe 890 ngàn | Giải trí (2.4tr)<br>Đi lại (890k) | Chưa xác định (2370.0tr)<br>Chưa xác định (890k) | ❌ | ❌ Missed: Giải trí<br>✅ Đi lại<br>⚠️ Extra: Chưa xác định |
| 129 | đi cf hết 480000 | Ăn uống (480k) | Ăn uống (480k) | ✅ | ✅ Ăn uống |
| 130 | thu son 600.000 | Mua sắm (600k) | Chưa xác định (600k) | ✅ | ✅ Mua sắm |
| 131 | 540k son | Mua sắm (540k) | Mua sắm (540k) | ✅ | ✅ Mua sắm |
| 132 | đi vở hết 8.220.000 | Giáo dục (8.2tr) | Mua sắm (8.2tr) | ✅ | ✅ Giáo dục |
| 133 | đi nước muối hết 1510 ngàn | Y tế (1.5tr) | Y tế (1.5tr) | ✅ | ✅ Y tế |
| 134 | thu bảo hiểm y tế 1.89m | Y tế (1.9tr) | Y tế (1.9tr) | ✅ | ✅ Y tế |
| 135 | 3920k tiền spotify | Giải trí (3.9tr) | Giải trí (3.9tr) | ✅ | ✅ Giải trí |
| 136 | di tap chi het 2560 canh | Mua sắm (2.6tr) | Chưa xác định (2.6tr) | ✅ | ✅ Mua sắm |
| 137 | sua xe 1.69tr | Đi lại (1.7tr) | Chưa xác định (1.7tr) | ✅ | ✅ Đi lại |
| 138 | mua học phí 7400000 | Giáo dục (7.4tr) | Giáo dục (7.4tr) | ✅ | ✅ Giáo dục |
| 139 | 390 cành tiền quần áo cộng tiền công 17300 cành | Mua sắm (390k)<br>Thu nhập (17.3tr) | Mua sắm (390k)<br>Thu nhập (1.7tr) | ✅ | ✅ Mua sắm<br>✅ Thu nhập |
| 140 | karaoke 3.770.000 | Giải trí (3.8tr) | Giải trí (3.8tr) | ✅ | ✅ Giải trí |
| 141 | nhậu 310 cành, 1970k bảo dưỡng xe | Ăn uống (310k)<br>Đi lại (2.0tr) | Chưa xác định (310k)<br>Đi lại (2.0tr) | ✅ | ✅ Ăn uống<br>✅ Đi lại |
| 142 | đi thưởng hết 7410k | Thu nhập (7.4tr) | Giải trí (7.4tr) | ✅ | ✅ Thu nhập |
| 143 | đi mỹ phẩm hết 2.780.000 | Mua sắm (2.8tr) | Mua sắm (2.8tr) | ✅ | ✅ Mua sắm |
| 144 | đi rau củ hết 400.000 | Mua sắm (400k) | Mua sắm (400k) | ✅ | ✅ Mua sắm |
| 145 | 1270 ngàn tiền viện phí | Y tế (1.3tr) | Y tế (1.3tr) | ✅ | ✅ Y tế |
| 146 | nhận du lịch 720k, nhận gửi xe 1070 cành, điện ... | Giải trí (720k)<br>Đi lại (1.1tr)<br>Nhà ở (2.6tr) | Chưa xác định (720k)<br>Chưa xác định (1.1tr)<br>Chưa xác định (2.6tr) | ✅ | ✅ Giải trí<br>✅ Đi lại<br>✅ Nhà ở |
| 147 | quan ao 2.440.000 với trả nhổ răng 1000 cành | Mua sắm (2.4tr)<br>Y tế (1.0tr) | Mua sắm (2.4tr)<br>Y tế (1.0tr) | ✅ | ✅ Mua sắm<br>✅ Y tế |
| 148 | đi khám răng hết 400 ngàn - wifi 1000000 | Y tế (400k)<br>Nhà ở (1.0tr) | Y tế (400k)<br>Chưa xác định (1.0tr) | ✅ | ✅ Y tế<br>✅ Nhà ở |
| 149 | vé xem phim 4130k | Giải trí (4.1tr) | Giải trí (4.1tr) | ✅ | ✅ Giải trí |
| 150 | di khoa hoc online het 540k | Giáo dục (540k) | Giáo dục (540k) | ✅ | ✅ Giáo dục |
| 151 | đi vở hết 7300 ngàn cộng 2310k tiền nhà | Giáo dục (7.3tr)<br>Nhà ở (2.3tr) | Chưa xác định (7.3tr)<br>Nhà ở (2.3tr) | ✅ | ✅ Giáo dục<br>✅ Nhà ở |
| 152 | di internet het 2370 canh | Nhà ở (2.4tr) | Chưa xác định (2.4tr) | ✅ | ✅ Nhà ở |
| 153 | đi xem phim hết 2790000 | Giải trí (2.8tr) | Giải trí (2.8tr) | ✅ | ✅ Giải trí |
| 154 | 430 cành cơm tấm | Ăn uống (430k) | Ăn uống (430k) | ✅ | ✅ Ăn uống |
| 155 | đi tạp chí hết 790 cành | Mua sắm (790k) | Chưa xác định (790k) | ✅ | ✅ Mua sắm |
| 156 | giày 2.37 triệu | Mua sắm (2.4tr) | Mua sắm (2.4tr) | ✅ | ✅ Mua sắm |
| 157 | mua hủ tiếu 390k | Ăn uống (390k) | Ăn uống (390k) | ✅ | ✅ Ăn uống |
| 158 | di karaoke het 600k | Giải trí (600k) | Giải trí (600k) | ✅ | ✅ Giải trí |
| 159 | gas 1870 cành và 170 cành tiền quần áo | Nhà ở (1.9tr)<br>Mua sắm (170k) | Chưa xác định (1.9tr)<br>Mua sắm (170k) | ✅ | ✅ Nhà ở<br>✅ Mua sắm |
| 160 | được hoàn tiền 1670000 - thu bóng đèn 1360000 r... | Thu nhập (1.7tr)<br>Nhà ở (1.4tr)<br>Mua sắm (1.4tr) | Chưa xác định (1.7tr)<br>Mua sắm (1.4tr)<br>Mua sắm (1.4tr) | ✅ | ✅ Thu nhập<br>✅ Nhà ở<br>✅ Mua sắm |
| 161 | trả trà sữa 120.000 lúc nãy. đi sinh tố hết 460... | Ăn uống (120k)<br>Ăn uống (460k) | Ăn uống (120k)<br>Ăn uống (460k) | ✅ | ✅ Ăn uống<br>✅ Ăn uống |
| 162 | khám răng 940k | Y tế (940k) | Y tế (940k) | ✅ | ✅ Y tế |
| 163 | sách 220 cành | Mua sắm (220k) | Chưa xác định (220k) | ✅ | ✅ Mua sắm |
| 164 | dụng cụ học tập 5.310.000 | Giáo dục (5.3tr) | Giáo dục (5.3tr) | ✅ | ✅ Giáo dục |
| 165 | 2470 ngàn tiền spotify, hủ tiếu 260 cành rồi 1.... | Giải trí (2.5tr)<br>Ăn uống (260k)<br>Y tế (1.8tr) | Giải trí (2.5tr)<br>Ăn uống (260k)<br>Nhà ở (1.8tr) | ✅ | ✅ Giải trí<br>✅ Ăn uống<br>✅ Y tế |
| 166 | đi nhổ răng hết 1.57m | Y tế (1.6tr) | Y tế (1.6tr) | ✅ | ✅ Y tế |
| 167 | son 790k | Mua sắm (790k) | Chưa xác định (790k) | ✅ | ✅ Mua sắm |
| 168 | du lich 2160k | Giải trí (2.2tr) | Chưa xác định (2.2tr) | ✅ | ✅ Giải trí |
| 169 | 1390 cành tiền bảo hiểm y tế rồi 15950 ngàn đượ... | Y tế (1.4tr)<br>Thu nhập (15.9tr) | Y tế (1.4tr)<br>Thu nhập (15.9tr) | ✅ | ✅ Y tế<br>✅ Thu nhập |
| 170 | nhận bowling 2.57m | Giải trí (2.6tr) | Giải trí (2.6tr) | ✅ | ✅ Giải trí |
| 171 | nhận toeic 8540000 | Giáo dục (8.5tr) | Giáo dục (8.5tr) | ✅ | ✅ Giáo dục |
| 172 | khau trang 920.000 | Y tế (920k) | Mua sắm (920k) | ✅ | ✅ Y tế |
| 173 | thanh toán grab 710 cành | Đi lại (710k) | Đi lại (710k) | ✅ | ✅ Đi lại |
| 174 | chi dầu gội 1750000 | Mua sắm (1.8tr) | Mua sắm (1.8tr) | ✅ | ✅ Mua sắm |
| 175 | vừa nước muối 1.940.000 | Y tế (1.9tr) | Chưa xác định (1.9tr) | ✅ | ✅ Y tế |
| 176 | khẩu trang 1.91 triệu | Y tế (1.9tr) | Mua sắm (1.9tr) | ✅ | ✅ Y tế |
| 177 | rửa xe 310.000 | Đi lại (310k) | Chưa xác định (310k) | ✅ | ✅ Đi lại |
| 178 | son 1.98m | Mua sắm (2.0tr) | { "nội dung": "Son cao 1.98m ư?", "số tiền": "98đ"} (98đ) | ❌ | ❌ Missed: Mua sắm<br>⚠️ Extra: { "nội dung": "Son cao 1.98m ư?", "số tiền": "98đ"} |
| 179 | ielts 6.410.000 rồi 3.26 triệu tiền tiền trọ | Giáo dục (6.4tr)<br>Nhà ở (3.3tr) | Giáo dục (6.4tr)<br>Nhà ở (3.3tr) | ✅ | ✅ Giáo dục<br>✅ Nhà ở |
| 180 | 2.820.000 tien spotify | Giải trí (2.8tr) | Giải trí (2.8tr) | ✅ | ✅ Giải trí |
| 181 | vé xe 440k | Đi lại (440k) | Đi lại (440k) | ✅ | ✅ Đi lại |
| 182 | 1310 cành tiền karaoke | Giải trí (1.3tr) | Giải trí (13.1tr) | ✅ | ✅ Giải trí |
| 183 | rác 4140 cành | Nhà ở (4.1tr) | Chưa xác định (4k) | ❌ | ❌ Missed: Nhà ở<br>⚠️ Extra: Chưa xác định |
| 184 | đi phở hết 140 cành thêm bowling 2.36 triệu | Ăn uống (140k)<br>Giải trí (2.4tr) | Ăn uống (140k)<br>Giải trí (2.4tr) | ✅ | ✅ Ăn uống<br>✅ Giải trí |
| 185 | 1450k tiền túi xách và được cho 1550000 | Mua sắm (1.4tr)<br>Thu nhập (1.6tr) | Mua sắm (1.4tr)<br>Thu nhập (1.6tr) | ✅ | ✅ Mua sắm<br>✅ Thu nhập |
| 186 | bút 3.53 triệu | Giáo dục (3.5tr) | Mua sắm (3.5tr) | ✅ | ✅ Giáo dục |
| 187 | đi sữa tắm hết 1460 ngàn | Mua sắm (1.5tr) | Mua sắm (1.5tr) | ✅ | ✅ Mua sắm |
| 188 | đóng internet 2360000 | Nhà ở (2.4tr) | Chưa xác định (2.4tr) | ✅ | ✅ Nhà ở |
| 189 | 4980 ngàn tiền vé xem phim rồi vừa xe ôm 440 ng... | Giải trí (5.0tr)<br>Đi lại (440k)<br>Đi lại (1.8tr) | Giải trí (5.0tr)<br>Đi lại (440k)<br>Nhà ở (1.8tr) | ✅ | ✅ Giải trí<br>✅ Đi lại<br>✅ Đi lại |
| 190 | đóng xăng 760000 | Đi lại (760k) | Đi lại (760k) | ✅ | ✅ Đi lại |
| 191 | đi nước hết 4.06tr | Nhà ở (4.1tr) | Chưa xác định (4.1tr) | ✅ | ✅ Nhà ở |
| 192 | đi lì xì hết 13800000 rồi sửa xe 1810 ngàn | Thu nhập (13.8tr)<br>Đi lại (1.8tr) | Chưa xác định (13.8tr)<br>Chưa xác định (1.8tr) | ✅ | ✅ Thu nhập<br>✅ Đi lại |
| 193 | toeic 95 cành | Giáo dục (95k) | Chưa xác định (950k) | ❌ | ❌ Missed: Giáo dục<br>⚠️ Extra: Chưa xác định |
| 194 | lương được cho 14.330.000, bia 380 ngàn rồi 486... | Thu nhập (14.3tr)<br>Ăn uống (380k)<br>Giáo dục (4.9tr) | Thu nhập (14.3tr)<br>Ăn uống (380k)<br>Giáo dục (4.9tr) | ✅ | ✅ Thu nhập<br>✅ Ăn uống<br>✅ Giáo dục |
| 195 | đi bán đồ cũ hết 10570 ngàn | Thu nhập (10.6tr) | Chưa xác định (10.6tr) | ✅ | ✅ Thu nhập |
| 196 | gojek 1690 ngàn | Đi lại (1.7tr) | Đi lại (1.7tr) | ✅ | ✅ Đi lại |
| 197 | đi viện phí hết 1.290.000 - đi taxi hết 1.45m | Y tế (1.3tr)<br>Đi lại (1.4tr) | Y tế (1.3tr)<br>Đi lại (1.4tr) | ✅ | ✅ Y tế<br>✅ Đi lại |
| 198 | được cho 10.38 triệu | Thu nhập (10.4tr) | Thu nhập (10.4tr) | ✅ | ✅ Thu nhập |
| 199 | bún bò 290000 | Ăn uống (290k) | Ăn uống (290k) | ✅ | ✅ Ăn uống |
| 200 | có lãi ngân hàng 9.290.000 | Thu nhập (9.3tr) | Thu nhập (9.3tr) | ✅ | ✅ Thu nhập |
| 201 | netflix 3640000 và 3.450.000 tiền photo tài liệu | Giải trí (3.6tr)<br>Giáo dục (3.5tr) | Giải trí (3.6tr)<br>Chưa xác định (3.5tr) | ✅ | ✅ Giải trí<br>✅ Giáo dục |
| 202 | mua khẩu trang 1870 ngàn tối qua. vừa spotify 4... | Y tế (1.9tr)<br>Giải trí (4.8tr) | Mua sắm (1.9tr)<br>Giải trí (4.8tr) | ✅ | ✅ Y tế<br>✅ Giải trí |
| 203 | cơm tấm 30 ngàn | Ăn uống (30k) | Ăn uống (30k) | ✅ | ✅ Ăn uống |
| 204 | lương lãi ngân hàng 13.260.000 rồi 1.55m tiền đ... | Thu nhập (13.3tr)<br>Mua sắm (1.6tr) | Thu nhập (13.3tr)<br>Mua sắm (1.6tr) | ✅ | ✅ Thu nhập<br>✅ Mua sắm |
| 205 | đi vé máy bay hết 1.92m | Đi lại (1.9tr) | Đi lại (1.9tr) | ✅ | ✅ Đi lại |
| 206 | co duoc cho 15060k | Thu nhập (15.1tr) | Thu nhập (15.1tr) | ✅ | ✅ Thu nhập |
| 207 | siêu thị 2.9m | Mua sắm (2.9tr) | Mua sắm (2.9tr) | ✅ | ✅ Mua sắm |
| 208 | vừa dụng cụ học tập 7.32m trưa nay | Giáo dục (7.3tr) | Giáo dục (7.3tr)<br>Chưa xác định (0đ) | ❌ | ✅ Giáo dục<br>⚠️ Extra: Chưa xác định |
| 209 | 2020000 tiền mỹ phẩm | Mua sắm (2.0tr) | Mua sắm (2.0tr) | ✅ | ✅ Mua sắm |
| 210 | di lai ngan hang het 15.380.000, wifi 4390000 | Thu nhập (15.4tr)<br>Nhà ở (4.4tr) | Chưa xác định (15.4tr)<br>Chưa xác định (4.4tr) | ✅ | ✅ Thu nhập<br>✅ Nhà ở |
| 211 | thưởng 12.300.000 | Thu nhập (12.3tr) | Thu nhập (12.3tr) | ✅ | ✅ Thu nhập |
| 212 | thu wifi 4560k, đi được cho hết 1.42 triệu - có... | Nhà ở (4.6tr)<br>Thu nhập (1.4tr)<br>Thu nhập (8.4tr) | Chưa xác định (4.6tr)<br>Chưa xác định (1.4tr)<br>Chưa xác định (8.4tr) | ✅ | ✅ Nhà ở<br>✅ Thu nhập<br>✅ Thu nhập |
| 213 | 110 ngàn tiền phở | Ăn uống (110k) | Ăn uống (110k) | ✅ | ✅ Ăn uống |
| 214 | 200k trà sữa | Ăn uống (200k) | Ăn uống (200k) | ✅ | ✅ Ăn uống |
| 215 | 840000 dịch vụ chung cư. bus 1950k chiều nay | Nhà ở (840k)<br>Đi lại (1.9tr) | Nhà ở (840k)<br>Đi lại (1.9tr) | ✅ | ✅ Nhà ở<br>✅ Đi lại |
| 216 | đi gas hết 4870k. xe ôm 1490k | Nhà ở (4.9tr)<br>Đi lại (1.5tr) | Chưa xác định (4.9tr)<br>Đi lại (1.5tr) | ✅ | ✅ Nhà ở<br>✅ Đi lại |
| 217 | đi book vé hết 3.21 triệu | Giải trí (3.2tr) | Chưa xác định (3.2tr) | ✅ | ✅ Giải trí |
| 218 | bóng đèn 4.29tr | Nhà ở (4.3tr) | Mua sắm (4.3tr) | ✅ | ✅ Nhà ở |
| 219 | khẩu trang 1420000 | Y tế (1.4tr) | Mua sắm (1.4tr) | ✅ | ✅ Y tế |
| 220 | bia 280 ngàn | Ăn uống (280k) | Ăn uống (280k) | ✅ | ✅ Ăn uống |
| 221 | đi cà phê hết 140.000 | Ăn uống (140k) | Ăn uống (140k) | ✅ | ✅ Ăn uống |
| 222 | nước muối 540 cành | Y tế (540k) | Chưa xác định (540k) | ✅ | ✅ Y tế |
| 223 | spotify 3420k | Giải trí (3.4tr) | Giải trí (3.4tr) | ✅ | ✅ Giải trí |
| 224 | my pham 2.620.000. đi mỹ phẩm hết 330k với đi k... | Mua sắm (2.6tr)<br>Mua sắm (330k)<br>Y tế (1.1tr) | Chưa xác định (2.6tr)<br>Mua sắm (330k)<br>Y tế (1.1tr) | ❌ | ✅ Mua sắm<br>❌ Missed: Mua sắm<br>✅ Y tế<br>⚠️ Extra: Chưa xác định |
| 225 | 1.71 triệu khẩu trang | Y tế (1.7tr) | Chưa xác định (1.7tr) | ✅ | ✅ Y tế |
| 226 | đi giày hết 1.290.000 | Mua sắm (1.3tr) | Mua sắm (1.3tr) | ✅ | ✅ Mua sắm |
| 227 | đóng khám bệnh 1570000 | Y tế (1.6tr) | Y tế (1.6tr) | ✅ | ✅ Y tế |
| 228 | gửi xe 480000 | Đi lại (480k) | Đi lại (480k) | ✅ | ✅ Đi lại |
| 229 | siêu thị 590.000 | Mua sắm (590k) | Mua sắm (590k) | ✅ | ✅ Mua sắm |
| 230 | trả bus 610k | Đi lại (610k) | Đi lại (610k) | ✅ | ✅ Đi lại |
| 231 | 4.33 triệu tiền dụng cụ học tập | Giáo dục (4.3tr) | Giáo dục (4.3tr) | ✅ | ✅ Giáo dục |
| 232 | đi tạp chí hết 2.68m | Mua sắm (2.7tr) | Mua sắm (2.7tr) | ✅ | ✅ Mua sắm |
| 233 | thu váy 2250000 | Mua sắm (2.3tr) | Mua sắm (2.3tr) | ✅ | ✅ Mua sắm |
| 234 | đi bún bò hết 160000 | Ăn uống (160k) | Ăn uống (160k) | ✅ | ✅ Ăn uống |
| 235 | tạp chí 1260000 | Mua sắm (1.3tr) | Giải trí (1.3tr) | ✅ | ✅ Mua sắm |
| 236 | đi siêu thị hết 2240000 | Mua sắm (2.2tr) | Mua sắm (2.2tr) | ✅ | ✅ Mua sắm |
| 237 | nhậu 230 cành, đi rác hết 2060 ngàn | Ăn uống (230k)<br>Nhà ở (2.1tr) | Ăn uống (230k)<br>Chưa xác định (2.1tr) | ✅ | ✅ Ăn uống<br>✅ Nhà ở |
| 238 | đi tiền nhà hết 1.25 triệu - book vé 3.57m sau ... | Nhà ở (1.3tr)<br>Giải trí (3.6tr)<br>Ăn uống (290k) | Chưa xác định (1.3tr)<br>Chưa xác định (3.6tr)<br>Ăn uống (290k) | ✅ | ✅ Nhà ở<br>✅ Giải trí<br>✅ Ăn uống |
| 239 | thanh toán youtube premium 4190 ngàn | Giải trí (4.2tr) | Giải trí (4.2tr) | ✅ | ✅ Giải trí |
| 240 | be 1530k | Đi lại (1.5tr) | Chưa xác định (1.5tr) | ✅ | ✅ Đi lại |
| 241 | 1.92 triệu tiền đi chợ | Mua sắm (1.9tr) | Mua sắm (1.9tr) | ✅ | ✅ Mua sắm |
| 242 | được lãi ngân hàng 9860k thêm grab 1.240.000. t... | Thu nhập (9.9tr)<br>Đi lại (1.2tr)<br>Y tế (1.3tr) | Thu nhập (9.9tr)<br>Đi lại (1.2tr)<br>Y tế (1.3tr) | ✅ | ✅ Thu nhập<br>✅ Đi lại<br>✅ Y tế |
| 243 | đi bus hết 1530 ngàn | Đi lại (1.5tr) | Đi lại (1.5tr) | ✅ | ✅ Đi lại |
| 244 | xăng 1910 ngàn sau đó 2930k tiền photo tài liệu | Đi lại (1.9tr)<br>Giáo dục (2.9tr) | Đi lại (1.9tr)<br>Giáo dục (2.9tr) | ✅ | ✅ Đi lại<br>✅ Giáo dục |
| 245 | đi du lịch hết 4930k | Giải trí (4.9tr) | Giải trí (4.9tr) | ✅ | ✅ Giải trí |
| 246 | mới rửa xe 1090k | Đi lại (1.1tr) | Chưa xác định (1.1tr) | ✅ | ✅ Đi lại |
| 247 | be 1.000.000 | Đi lại (1.0tr) | Chưa xác định (1.0tr) | ✅ | ✅ Đi lại |
| 248 | nhận internet 4460 cành | Nhà ở (4.5tr) | Chưa xác định (4k) | ❌ | ❌ Missed: Nhà ở<br>⚠️ Extra: Chưa xác định |
| 249 | rác 350 ngàn | Nhà ở (350k) | Chưa xác định (350k) | ✅ | ✅ Nhà ở |
| 250 | 1.56tr tiền karaoke | Giải trí (1.6tr) | Giải trí (1.6tr) | ✅ | ✅ Giải trí |
| 251 | đi đòi nợ hết 2150 cành | Thu nhập (2.1tr) | Chưa xác định (2.1tr) | ✅ | ✅ Thu nhập |
| 252 | trà sữa 110 ngàn | Ăn uống (110k) | Ăn uống (110k) | ✅ | ✅ Ăn uống |
| 253 | được tiền công 7890000 | Thu nhập (7.9tr) | Thu nhập (7.9tr) | ✅ | ✅ Thu nhập |
| 254 | lì xì 16.28m rồi sách 210k | Thu nhập (16.3tr)<br>Mua sắm (210k) | Chưa xác định (16.3tr)<br>Giáo dục (210k) | ✅ | ✅ Thu nhập<br>✅ Mua sắm |
| 255 | 9860k vở | Giáo dục (9.9tr) | Chưa xác định (9.9tr) | ✅ | ✅ Giáo dục |
| 256 | đóng tiền học 3570 cành | Giáo dục (3.6tr) | Giáo dục (3.6tr) | ✅ | ✅ Giáo dục |
| 257 | thu kính thuốc 390.000 lúc nãy và đi taxi hết 1... | Y tế (390k)<br>Đi lại (1.0tr) | Y tế (390k)<br>Đi lại (1.0tr) | ✅ | ✅ Y tế<br>✅ Đi lại |
| 258 | internet 570k | Nhà ở (570k) | Chưa xác định (570k) | ✅ | ✅ Nhà ở |
| 259 | đi lãi ngân hàng hết 14.97 triệu | Thu nhập (15.0tr) | Thu nhập (15.0tr) | ✅ | ✅ Thu nhập |
| 260 | gà rán 100 ngàn | Ăn uống (100k) | Ăn uống (100k) | ✅ | ✅ Ăn uống |
| 261 | grab 1860000 | Đi lại (1.9tr) | Đi lại (1.9tr) | ✅ | ✅ Đi lại |
| 262 | thu vé máy bay 620 ngàn sau đó đi book vé hết 2... | Đi lại (620k)<br>Giải trí (2.8tr) | Chưa xác định (620k)<br>Chưa xác định (2.8tr) | ✅ | ✅ Đi lại<br>✅ Giải trí |
| 263 | mua học phí 4310 ngàn | Giáo dục (4.3tr) | Giáo dục (4.3tr) | ✅ | ✅ Giáo dục |
| 264 | spotify 980 ngàn | Giải trí (980k) | Giải trí (980k) | ✅ | ✅ Giải trí |
| 265 | đi nhổ răng hết 290.000 | Y tế (290k) | Y tế (290k) | ✅ | ✅ Y tế |
| 266 | đi sửa ống nước hết 4.180.000 | Nhà ở (4.2tr) | Nhà ở (4.2tr) | ✅ | ✅ Nhà ở |
| 267 | đi book vé hết 4310k thêm thu khau trang 210000 | Giải trí (4.3tr)<br>Y tế (210k) | Chưa xác định (4.3tr)<br>Chưa xác định (210k) | ✅ | ✅ Giải trí<br>✅ Y tế |
| 268 | 1480000 đổ xăng, đi gas hết 4.580.000 | Đi lại (1.5tr)<br>Nhà ở (4.6tr) | Đi lại (1.5tr)<br>Đi lại (4.6tr) | ✅ | ✅ Đi lại<br>✅ Nhà ở |
| 269 | 1.89tr váy - 1.150.000 xem phim | Mua sắm (1.9tr)<br>Giải trí (1.1tr) | Mua sắm (1.9tr)<br>Giải trí (1.1tr) | ✅ | ✅ Mua sắm<br>✅ Giải trí |
| 270 | đi bút hết 4.16m | Giáo dục (4.2tr) | Mua sắm (4.2tr) | ✅ | ✅ Giáo dục |
| 271 | đi trà sữa hết 430 cành | Ăn uống (430k) | Ăn uống (430k) | ✅ | ✅ Ăn uống |
| 272 | du lịch 900.000 | Giải trí (900k) | Giải trí (900k) | ✅ | ✅ Giải trí |
| 273 | đi lương hết 6580 ngàn, đi dầu gội hết 1010 cành | Thu nhập (6.6tr)<br>Mua sắm (1.0tr) | Thu nhập (6.6tr)<br>Y tế (1.0tr) | ✅ | ✅ Thu nhập<br>✅ Mua sắm |
| 274 | chi vé xem phim 140000 hôm kia thêm bowling 192... | Giải trí (140k)<br>Giải trí (1.9tr)<br>Y tế (840k) | Giải trí (140k)<br>Giải trí (1.9tr)<br>Y tế (840k) | ✅ | ✅ Giải trí<br>✅ Giải trí<br>✅ Y tế |
| 275 | 2440k tiền game sau đó mới rác 2060 ngàn tối qua | Giải trí (2.4tr)<br>Nhà ở (2.1tr) | Giải trí (2.4tr)<br>Chưa xác định (2.1tr) | ✅ | ✅ Giải trí<br>✅ Nhà ở |
| 276 | 3.760.000 tiền spotify - 2180 ngàn tiền youtube... | Giải trí (3.8tr)<br>Giải trí (2.2tr)<br>Giải trí (1.6tr) | Giải trí (3.8tr)<br>Giải trí (2.2tr)<br>Ăn uống (1.6tr) | ✅ | ✅ Giải trí<br>✅ Giải trí<br>✅ Giải trí |
| 277 | chi pizza 230000 | Ăn uống (230k) | Ăn uống (230k) | ✅ | ✅ Ăn uống |
| 278 | vừa wifi 3300k tối qua sau đó khóa học online 5... | Nhà ở (3.3tr)<br>Giáo dục (5.1tr) | Chưa xác định (3.3tr)<br>Giáo dục (5.1tr) | ✅ | ✅ Nhà ở<br>✅ Giáo dục |
| 279 | thu kính thuốc 350k | Y tế (350k) | Y tế (350k) | ✅ | ✅ Y tế |
| 280 | cafe 470k | Ăn uống (470k) | Ăn uống (470k) | ✅ | ✅ Ăn uống |
| 281 | trà sữa 85.000 và đi thuốc hết 1.35m | Ăn uống (85k)<br>Y tế (1.4tr) | Ăn uống (85k)<br>Y tế (1.4tr) | ✅ | ✅ Ăn uống<br>✅ Y tế |
| 282 | netflix 890 cành | Giải trí (890k) | Giải trí (890k) | ✅ | ✅ Giải trí |
| 283 | đi vở hết 2.5 triệu | Giáo dục (2.5tr) | Mua sắm (2.5tr) | ✅ | ✅ Giáo dục |
| 284 | di ban do cu het 9.37 trieu | Thu nhập (9.4tr) | Chưa xác định (9.4tr) | ✅ | ✅ Thu nhập |
| 285 | đi bowling hết 1430k | Giải trí (1.4tr) | Giải trí (1.4tr) | ✅ | ✅ Giải trí |
| 286 | trả ielts 9.06tr rồi đi gửi xe hết 1480k | Giáo dục (9.1tr)<br>Đi lại (1.5tr) | Giáo dục (9.1tr)<br>Đi lại (1.5tr) | ✅ | ✅ Giáo dục<br>✅ Đi lại |
| 287 | đi siêu thị hết 2.180.000 thêm lương thưởng 110... | Mua sắm (2.2tr)<br>Thu nhập (11.1tr)<br>Thu nhập (6.3tr) | Mua sắm (2.2tr)<br>Thu nhập (11.1tr)<br>Thu nhập (6k) | ✅ | ✅ Mua sắm<br>✅ Thu nhập<br>✅ Thu nhập |
| 288 | thanh toán spotify 1.540.000 | Giải trí (1.5tr) | Giải trí (1.5tr) | ✅ | ✅ Giải trí |
| 289 | 1.47tr be | Đi lại (1.5tr) | Chưa xác định (1.5tr) | ✅ | ✅ Đi lại |
| 290 | vừa spotify 1480000 | Giải trí (1.5tr) | Giải trí (1.5tr) | ✅ | ✅ Giải trí |
| 291 | xem phim 3.310.000 | Giải trí (3.3tr) | Giải trí (3.3tr) | ✅ | ✅ Giải trí |
| 292 | đi khẩu trang hết 360 ngàn | Y tế (360k) | Mua sắm (360k) | ✅ | ✅ Y tế |
| 293 | đi pizza hết 370 ngàn | Ăn uống (370k) | Ăn uống (370k) | ✅ | ✅ Ăn uống |
| 294 | đi xem phim hết 4.010.000 sau đó đi gas hết 427... | Giải trí (4.0tr)<br>Nhà ở (4.3tr)<br>Nhà ở (360k) | Giải trí (4.0tr)<br>Đi lại (4.3tr)<br>Nhà ở (360k) | ❌ | ✅ Giải trí<br>✅ Nhà ở<br>❌ Missed: Nhà ở<br>⚠️ Extra: Đi lại |
| 295 | 75 ngàn rửa xe | Đi lại (75k) | Chưa xác định (75k) | ✅ | ✅ Đi lại |
| 296 | được lãi ngân hàng 780.000, 9.02tr toeic với xé... | Thu nhập (780k)<br>Giáo dục (9.0tr)<br>Y tế (1.6tr) | Thu nhập (780k)<br>Thu nhập (9.0tr)<br>Y tế (1.6tr) | ✅ | ✅ Thu nhập<br>✅ Giáo dục<br>✅ Y tế |
| 297 | trả sữa tắm 1490k | Mua sắm (1.5tr) | Mua sắm (1.5tr) | ✅ | ✅ Mua sắm |
| 298 | chi vé máy bay 180.000 thêm đi được cho hết 131... | Đi lại (180k)<br>Thu nhập (13.1tr) | Chưa xác định (180k)<br>Chưa xác định (13.1tr) | ✅ | ✅ Đi lại<br>✅ Thu nhập |
| 299 | đóng túi xách 95.000 lúc nãy | Mua sắm (95k) | Chưa xác định (95k) | ✅ | ✅ Mua sắm |
| 300 | chi tien nha 2.81m | Nhà ở (2.8tr) | Nhà ở (2.8tr) | ✅ | ✅ Nhà ở |
| 301 | di ve xe het 1400 ngan | Đi lại (1.4tr) | Đi lại (1.4tr) | ✅ | ✅ Đi lại |
| 302 | doi no 9.77 trieu | Thu nhập (9.8tr) | Chưa xác định (9.8tr) | ✅ | ✅ Thu nhập |
| 303 | áo thun 1820000 | Mua sắm (1.8tr) | Mua sắm (1.8tr) | ✅ | ✅ Mua sắm |
| 304 | 6.14 triệu bút | Giáo dục (6.1tr) | Chưa xác định (6.1tr) | ✅ | ✅ Giáo dục |
| 305 | đóng vé máy bay 280.000 hôm kia | Đi lại (280k) | Đi lại (280k) | ✅ | ✅ Đi lại |
| 306 | 10.830.000 lì xì | Thu nhập (10.8tr) | Thu nhập (10.8tr) | ✅ | ✅ Thu nhập |
| 307 | đi bắp nước hết 2.960.000 | Giải trí (3.0tr) | Ăn uống (3.0tr) | ✅ | ✅ Giải trí |
| 308 | viện phí 670.000 | Y tế (670k) | Y tế (670k) | ✅ | ✅ Y tế |
| 309 | chi netflix 2.3tr chiều nay, được lương 7580 ngàn | Giải trí (2.3tr)<br>Thu nhập (7.6tr) | Giải trí (2.3tr)<br>Thu nhập (7.6tr) | ✅ | ✅ Giải trí<br>✅ Thu nhập |
| 310 | 1870k tiền khẩu trang | Y tế (1.9tr) | Y tế (1.9tr) | ✅ | ✅ Y tế |
| 311 | thu túi xách 1.22 triệu với lương lãi ngân hàng... | Mua sắm (1.2tr)<br>Thu nhập (19.3tr) | Mua sắm (1.2tr)<br>Thu nhập (19.3tr) | ✅ | ✅ Mua sắm<br>✅ Thu nhập |
| 312 | chi bảo hiểm y tế 95 ngàn sáng nay | Y tế (95k) | Y tế (95k) | ✅ | ✅ Y tế |
| 313 | tiền học 3.22 triệu | Giáo dục (3.2tr) | Giáo dục (3.2tr) | ✅ | ✅ Giáo dục |
| 314 | 480.000 vé máy bay | Đi lại (480k) | Đi lại (480k) | ✅ | ✅ Đi lại |
| 315 | di dien het 4740 canh | Nhà ở (4.7tr) | Chưa xác định (4.7tr) | ✅ | ✅ Nhà ở |
| 316 | đi rác hết 2740 ngàn với thanh toán nước muối 1... | Nhà ở (2.7tr)<br>Y tế (1.0tr)<br>Nhà ở (4.4tr) | Chưa xác định (2.7tr)<br>Chưa xác định (1.0tr)<br>Chưa xác định (4.4tr) | ✅ | ✅ Nhà ở<br>✅ Y tế<br>✅ Nhà ở |
| 317 | đi rác hết 1.650.000 | Nhà ở (1.6tr) | Chưa xác định (1.6tr) | ✅ | ✅ Nhà ở |
| 318 | 4590k tien tien nha | Nhà ở (4.6tr) | Chưa xác định (4.6tr) | ✅ | ✅ Nhà ở |
| 319 | kham benh 540000 | Y tế (540k) | Y tế (540k) | ✅ | ✅ Y tế |
| 320 | rau củ 2.560.000 | Mua sắm (2.6tr) | Mua sắm (2.6tr) | ✅ | ✅ Mua sắm |
| 321 | thanh toán học phí 1570000 | Giáo dục (1.6tr) | Giáo dục (1.6tr) | ✅ | ✅ Giáo dục |
| 322 | trả xăng 210 ngàn | Đi lại (210k) | Đi lại (210k) | ✅ | ✅ Đi lại |
| 323 | đi đổ xăng hết 330 cành - khẩu trang 1.270.000 | Đi lại (330k)<br>Y tế (1.3tr) | Đi lại (330k)<br>Chưa xác định (1.3tr) | ✅ | ✅ Đi lại<br>✅ Y tế |
| 324 | nhau 150 canh - xe ôm 1930000 | Ăn uống (150k)<br>Đi lại (1.9tr) | Chưa xác định (150k)<br>Đi lại (1.9tr) | ✅ | ✅ Ăn uống<br>✅ Đi lại |
| 325 | be 1730 cành sau đó đi be hết 880.000 với 28800... | Đi lại (1.7tr)<br>Đi lại (880k)<br>Mua sắm (2.9tr) | Chưa xác định (2k)<br>Chưa xác định (880k)<br>Mua sắm (2.9tr) | ❌ | ❌ Missed: Đi lại<br>✅ Đi lại<br>✅ Mua sắm<br>⚠️ Extra: Chưa xác định |
| 326 | đi tiền trọ hết 2.11m và di ielts het 390 ngan,... | Nhà ở (2.1tr)<br>Giáo dục (390k)<br>Mua sắm (2.6tr) | Nhà ở (2.1tr)<br>Giáo dục (390k)<br>Mua sắm (2.6tr) | ✅ | ✅ Nhà ở<br>✅ Giáo dục<br>✅ Mua sắm |
| 327 | đi chợ 2170k cộng mới bus 1000 ngàn | Mua sắm (2.2tr)<br>Đi lại (1.0tr) | Mua sắm (2.2tr)<br>Đi lại (1.0tr) | ✅ | ✅ Mua sắm<br>✅ Đi lại |
| 328 | son 880000 | Mua sắm (880k) | Chưa xác định (880k) | ✅ | ✅ Mua sắm |
| 329 | áo thun 60 ngàn | Mua sắm (60k) | Mua sắm (60k) | ✅ | ✅ Mua sắm |
| 330 | vua rau cu 1870k | Mua sắm (1.9tr) | Chưa xác định (1.9tr) | ✅ | ✅ Mua sắm |
| 331 | kính thuốc 30 cành | Y tế (30k) | Y tế (300k) | ✅ | ✅ Y tế |
| 332 | 1.22tr ielts | Giáo dục (1.2tr) | Giáo dục (1.2tr) | ✅ | ✅ Giáo dục |
| 333 | vừa tiền nhà 3.920.000 với moi kham benh 230.000 | Nhà ở (3.9tr)<br>Y tế (230k) | Nhà ở (3.9tr)<br>Y tế (230k) | ✅ | ✅ Nhà ở<br>✅ Y tế |
| 334 | đi nước hết 710000 | Nhà ở (710k) | Chưa xác định (710k) | ✅ | ✅ Nhà ở |
| 335 | 75000 tiền sinh tố | Ăn uống (75k) | Y tế (75k) | ✅ | ✅ Ăn uống |
| 336 | đi photo tài liệu hết 3890k với mới bia 130 cành | Giáo dục (3.9tr)<br>Ăn uống (130k) | Chưa xác định (3.9tr)<br>Ăn uống (130k) | ✅ | ✅ Giáo dục<br>✅ Ăn uống |
| 337 | có thưởng 16.87 triệu hôm kia | Thu nhập (16.9tr) | Thu nhập (16.9tr) | ✅ | ✅ Thu nhập |
| 338 | thanh toán game 4050 cành hôm kia | Giải trí (4.0tr) | Chưa xác định (4k) | ❌ | ❌ Missed: Giải trí<br>⚠️ Extra: Chưa xác định |
| 339 | đi youtube premium hết 4420 cành rồi vừa viện p... | Giải trí (4.4tr)<br>Y tế (1.2tr) | Giải trí (4.4tr)<br>Y tế (1.2tr) | ✅ | ✅ Giải trí<br>✅ Y tế |
| 340 | đòi nợ 4.01tr | Thu nhập (4.0tr) | Thu nhập (4.0tr) | ✅ | ✅ Thu nhập |
| 341 | mua nước 3920 cành tối qua | Nhà ở (3.9tr) | Ăn uống (4k) | ❌ | ❌ Missed: Nhà ở<br>⚠️ Extra: Ăn uống |
| 342 | đóng nhậu 310k chiều nay rồi bowling 1.42tr | Ăn uống (310k)<br>Giải trí (1.4tr) | Ăn uống (310k)<br>Giải trí (1.4tr) | ✅ | ✅ Ăn uống<br>✅ Giải trí |
| 343 | 1430000 dầu gội rồi viện phí 1960k | Mua sắm (1.4tr)<br>Y tế (2.0tr) | Chưa xác định (1.4tr)<br>Chưa xác định (0đ)<br>Y tế (2.0tr) | ❌ | ✅ Mua sắm<br>✅ Y tế<br>⚠️ Extra: Chưa xác định |
| 344 | có thưởng 10.47m cộng nhận lãi ngân hàng 4.51m | Thu nhập (10.5tr)<br>Thu nhập (4.5tr) | Thu nhập (10.5tr)<br>Thu nhập (4.5tr) | ✅ | ✅ Thu nhập<br>✅ Thu nhập |
| 345 | cơm tấm 370.000 | Ăn uống (370k) | Ăn uống (370k) | ✅ | ✅ Ăn uống |
| 346 | đi dịch vụ chung cư hết 2370 ngàn | Nhà ở (2.4tr) | Nhà ở (2.4tr) | ✅ | ✅ Nhà ở |
| 347 | 5.870.000 tiền lương, 12510 ngàn tiền lãi ngân ... | Thu nhập (5.9tr)<br>Thu nhập (12.5tr) | Thu nhập (5.9tr)<br>Thu nhập (12.5tr) | ✅ | ✅ Thu nhập<br>✅ Thu nhập |
| 348 | đi taxi hết 1520 ngàn cộng mua đổ xăng 610 ngàn | Đi lại (1.5tr)<br>Đi lại (610k) | Đi lại (1.5tr)<br>Đi lại (610k) | ✅ | ✅ Đi lại<br>✅ Đi lại |
| 349 | sách giáo khoa 6.63tr rồi sửa ống nước 4.390.000 | Giáo dục (6.6tr)<br>Nhà ở (4.4tr) | Giáo dục (6.6tr)<br>Nhà ở (4.4tr) | ✅ | ✅ Giáo dục<br>✅ Nhà ở |
| 350 | đi xét nghiệm hết 1130k | Y tế (1.1tr) | Y tế (1.1tr) | ✅ | ✅ Y tế |
| 351 | gà rán 390000 | Ăn uống (390k) | Ăn uống (390k) | ✅ | ✅ Ăn uống |
| 352 | 1.480.000 tiền book vé | Giải trí (1.5tr) | Giải trí (1.5tr) | ✅ | ✅ Giải trí |
| 353 | đi bán đồ cũ hết 19680 cành - đi gojek hết 1550... | Thu nhập (19.7tr)<br>Đi lại (1.6tr) | Chưa xác định (20k)<br>Đi lại (1.6tr) | ❌ | ❌ Missed: Thu nhập<br>✅ Đi lại<br>⚠️ Extra: Chưa xác định |
| 354 | đi bia hết 60 ngàn | Ăn uống (60k) | Ăn uống (60k) | ✅ | ✅ Ăn uống |
| 355 | mua spotify 250 canh chieu nay | Giải trí (250k) | Giải trí (250k) | ✅ | ✅ Giải trí |
| 356 | karaoke 950 cành, vở 4.76m | Giải trí (950k)<br>Giáo dục (4.8tr) | Giải trí (950k)<br>Giáo dục (4.8tr) | ✅ | ✅ Giải trí<br>✅ Giáo dục |
| 357 | đi netflix hết 730.000 với đi tạp chí hết 1.180... | Giải trí (730k)<br>Mua sắm (1.2tr)<br>Đi lại (740k) | Giải trí (730k)<br>Mua sắm (1.2tr)<br>Đi lại (740k) | ✅ | ✅ Giải trí<br>✅ Mua sắm<br>✅ Đi lại |
| 358 | váy 870000 | Mua sắm (870k) | Mua sắm (870k) | ✅ | ✅ Mua sắm |
| 359 | tiền trọ 3.950.000 | Nhà ở (4.0tr) | Nhà ở (4.0tr) | ✅ | ✅ Nhà ở |
| 360 | 4030000 tiền nước | Nhà ở (4.0tr) | Chưa xác định (4.0tr) | ✅ | ✅ Nhà ở |
| 361 | nhận váy 320000 | Mua sắm (320k) | Mua sắm (320k) | ✅ | ✅ Mua sắm |
| 362 | chi bảo hiểm y tế 860000 | Y tế (860k) | Y tế (860k) | ✅ | ✅ Y tế |
| 363 | điện 4360k | Nhà ở (4.4tr) | Chưa xác định (4.4tr) | ✅ | ✅ Nhà ở |
| 364 | đi bảo hiểm y tế hết 1.760.000 sau đó mới bia 1... | Y tế (1.8tr)<br>Ăn uống (100k)<br>Mua sắm (780k) | Y tế (1.8tr)<br>Ăn uống (100k)<br>Chưa xác định (780k) | ✅ | ✅ Y tế<br>✅ Ăn uống<br>✅ Mua sắm |
| 365 | đi sửa ống nước hết 3640k | Nhà ở (3.6tr) | Nhà ở (3.6tr) | ✅ | ✅ Nhà ở |
| 366 | thu đi chợ 1220000. 1.630.000 ao thun | Mua sắm (1.2tr)<br>Mua sắm (1.6tr) | Chưa xác định (1.2tr)<br>Mua sắm (1.6tr) | ❌ | ✅ Mua sắm<br>❌ Missed: Mua sắm<br>⚠️ Extra: Chưa xác định |
| 367 | internet 3.620.000 | Nhà ở (3.6tr) | Chưa xác định (3.6tr) | ✅ | ✅ Nhà ở |
| 368 | vừa siêu thị 2.67tr và đóng gojek 1.8 triệu - đ... | Mua sắm (2.7tr)<br>Đi lại (1.8tr)<br>Nhà ở (3.1tr) | Mua sắm (2.7tr)<br>Đi lại (1.8tr)<br>Nhà ở (3.1tr) | ✅ | ✅ Mua sắm<br>✅ Đi lại<br>✅ Nhà ở |
| 369 | di khau trang het 1440 canh | Y tế (1.4tr) | Chưa xác định (14.4tr) | ❌ | ❌ Missed: Y tế<br>⚠️ Extra: Chưa xác định |
| 370 | đi trà sữa hết 230.000 và xôi 270.000 | Ăn uống (230k)<br>Ăn uống (270k) | Ăn uống (230k)<br>Ăn uống (270k) | ✅ | ✅ Ăn uống<br>✅ Ăn uống |
| 371 | photo tài liệu 9.91 triệu cộng be 1980 ngàn | Giáo dục (9.9tr)<br>Đi lại (2.0tr) | Chưa xác định (9.9tr)<br>Chưa xác định (2.0tr) | ✅ | ✅ Giáo dục<br>✅ Đi lại |
| 372 | vừa tiền học 480 cành với vừa photo tài liệu 60... | Giáo dục (480k)<br>Giáo dục (6.1tr) | Giáo dục (480k)<br>Chưa xác định (6.1tr) | ✅ | ✅ Giáo dục<br>✅ Giáo dục |
| 373 | 3880k tiền toeic | Giáo dục (3.9tr) | Giáo dục (3.9tr) | ✅ | ✅ Giáo dục |
| 374 | tiền nhà 2930 ngàn | Nhà ở (2.9tr) | Nhà ở (2.9tr) | ✅ | ✅ Nhà ở |
| 375 | mua đi chợ 1620 cành cộng đóng cơm tấm 450.000 ... | Mua sắm (1.6tr)<br>Ăn uống (450k) | Chưa xác định (1.6tr)<br>Ăn uống (450k) | ✅ | ✅ Mua sắm<br>✅ Ăn uống |
| 376 | 810000 dầu gội | Mua sắm (810k) | Mua sắm (810k) | ✅ | ✅ Mua sắm |
| 377 | phở 75 cành và vay 3000 ngan | Ăn uống (75k)<br>Mua sắm (3.0tr) | Ăn uống (75k)<br>Thu nhập (3.0tr) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 378 | tra bao duong xe 820 canh toi qua | Đi lại (820k) | Chưa xác định (820k) | ✅ | ✅ Đi lại |
| 379 | spotify 1710 ngàn | Giải trí (1.7tr) | Giải trí (1.7tr) | ✅ | ✅ Giải trí |
| 380 | vua thuoc 840 canh | Y tế (840k) | Chưa xác định (840k) | ✅ | ✅ Y tế |
| 381 | 1.57tr nước với túi xách 1.600.000 | Nhà ở (1.6tr)<br>Mua sắm (1.6tr) | Chưa xác định (1.6tr)<br>Mua sắm (1.6tr) | ✅ | ✅ Nhà ở<br>✅ Mua sắm |
| 382 | thu du lich 4.4 trieu | Giải trí (4.4tr) | Chưa xác định (4.4tr) | ✅ | ✅ Giải trí |
| 383 | thu khau trang 640000 - netflix 2500k | Y tế (640k)<br>Giải trí (2.5tr) | Chưa xác định (640k)<br>Giải trí (2.5tr) | ✅ | ✅ Y tế<br>✅ Giải trí |
| 384 | di tien nha het 3570k | Nhà ở (3.6tr) | Nhà ở (3.6tr) | ✅ | ✅ Nhà ở |
| 385 | đi bún bò hết 210000 | Ăn uống (210k) | Ăn uống (210k) | ✅ | ✅ Ăn uống |
| 386 | đi bán đồ cũ hết 3.030.000 | Thu nhập (3.0tr) | Chưa xác định (3.0tr) | ✅ | ✅ Thu nhập |
| 387 | 1820 ngàn tiền viện phí | Y tế (1.8tr) | Y tế (1.8tr) | ✅ | ✅ Y tế |
| 388 | được cho 14670 ngàn | Thu nhập (14.7tr) | Thu nhập (14.7tr) | ✅ | ✅ Thu nhập |
| 389 | đi bia hết 40000 | Ăn uống (40k) | Ăn uống (40k) | ✅ | ✅ Ăn uống |
| 390 | đi wifi hết 2890 ngàn cộng đi lãi ngân hàng hết... | Nhà ở (2.9tr)<br>Thu nhập (1.4tr) | Chưa xác định (2.9tr)<br>Thu nhập (1.4tr) | ✅ | ✅ Nhà ở<br>✅ Thu nhập |
| 391 | đi vở hết 1350000 | Giáo dục (1.4tr) | Mua sắm (1.4tr) | ✅ | ✅ Giáo dục |
| 392 | mới khám bệnh 1940000 | Y tế (1.9tr) | Y tế (1.9tr) | ✅ | ✅ Y tế |
| 393 | bánh mì 340 cành | Ăn uống (340k) | Ăn uống (340k) | ✅ | ✅ Ăn uống |
| 394 | 1230 canh tien xe om | Đi lại (1.2tr) | Chưa xác định (1.2tr)<br>Chưa xác định (0đ) | ❌ | ✅ Đi lại<br>⚠️ Extra: Chưa xác định |
| 395 | có hoàn tiền 11710000 | Thu nhập (11.7tr) | Thu nhập (11.7tr) | ✅ | ✅ Thu nhập |
| 396 | 1.72m tiền sách | Mua sắm (1.7tr) | Mua sắm (1.7tr) | ✅ | ✅ Mua sắm |
| 397 | thanh toán thuốc 790000 sau đó đi khám răng hết... | Y tế (790k)<br>Y tế (1.9tr) | Y tế (790k)<br>Y tế (2k) | ✅ | ✅ Y tế<br>✅ Y tế |
| 398 | đi nhổ răng hết 1.510.000, phở 490k | Y tế (1.5tr)<br>Ăn uống (490k) | Y tế (1.5tr)<br>Ăn uống (490k) | ✅ | ✅ Y tế<br>✅ Ăn uống |
| 399 | 2570000 tiền dịch vụ chung cư, mỹ phẩm 2960k | Nhà ở (2.6tr)<br>Mua sắm (3.0tr) | Nhà ở (2.6tr)<br>Mua sắm (3.0tr) | ✅ | ✅ Nhà ở<br>✅ Mua sắm |
| 400 | 2550 ngàn tiền son cộng bún bò 160.000 | Mua sắm (2.5tr)<br>Ăn uống (160k) | Mua sắm (2.5tr)<br>Ăn uống (160k) | ✅ | ✅ Mua sắm<br>✅ Ăn uống |
| 401 | mới dụng cụ học tập 9.430.000 | Giáo dục (9.4tr) | Giáo dục (9.4tr) | ✅ | ✅ Giáo dục |
| 402 | nhận hủ tiếu 290k | Ăn uống (290k) | Thu nhập (290k) | ✅ | ✅ Ăn uống |
| 403 | đi nước muối hết 770k | Y tế (770k) | Y tế (770k) | ✅ | ✅ Y tế |
| 404 | moi ielts 7.46 trieu thêm nhận khám bệnh 1810k | Giáo dục (7.5tr)<br>Y tế (1.8tr) | Giáo dục (7.5tr)<br>Y tế (1.8tr) | ✅ | ✅ Giáo dục<br>✅ Y tế |
| 405 | đóng gà rán 260 cành lúc nãy - sữa tắm 650 cành | Ăn uống (260k)<br>Mua sắm (650k) | Chưa xác định (260k)<br>Chưa xác định (650k) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 406 | 1.77 triệu grab - quần áo 1890000 | Đi lại (1.8tr)<br>Mua sắm (1.9tr) | Đi lại (1.8tr)<br>Mua sắm (1.9tr) | ✅ | ✅ Đi lại<br>✅ Mua sắm |
| 407 | mua phở 380 cành | Ăn uống (380k) | Ăn uống (380k) | ✅ | ✅ Ăn uống |
| 408 | đi pizza hết 50k | Ăn uống (50k) | Ăn uống (50k) | ✅ | ✅ Ăn uống |
| 409 | mua gas 2480 cành | Nhà ở (2.5tr) | Chưa xác định (2k) | ❌ | ❌ Missed: Nhà ở<br>⚠️ Extra: Chưa xác định |
| 410 | nhậu 370.000 sau đó khẩu trang 380 cành | Ăn uống (370k)<br>Y tế (380k) | Ăn uống (370k)<br>Mua sắm (380k) | ✅ | ✅ Ăn uống<br>✅ Y tế |
| 411 | xét nghiệm 1.040.000 | Y tế (1.0tr) | Y tế (1.0tr) | ✅ | ✅ Y tế |
| 412 | rác 160 ngàn. viện phí 1570 cành | Nhà ở (160k)<br>Y tế (1.6tr) | Chưa xác định (160k)<br>Y tế (1.6tr) | ✅ | ✅ Nhà ở<br>✅ Y tế |
| 413 | thanh toán internet 1470000, đi bus hết 1.040.000 | Nhà ở (1.5tr)<br>Đi lại (1.0tr) | Chưa xác định (1.5tr)<br>Đi lại (1.0tr) | ✅ | ✅ Nhà ở<br>✅ Đi lại |
| 414 | thanh toán khẩu trang 840 ngàn | Y tế (840k) | Y tế (840k) | ✅ | ✅ Y tế |
| 415 | khẩu trang 1.250.000 và 3.39tr netflix | Y tế (1.3tr)<br>Giải trí (3.4tr) | Chưa xác định (1.3tr)<br>Giải trí (3.4tr) | ✅ | ✅ Y tế<br>✅ Giải trí |
| 416 | 1750k taxi | Đi lại (1.8tr) | Đi lại (1.8tr) | ✅ | ✅ Đi lại |
| 417 | ielts 3.29 triệu | Giáo dục (3.3tr) | Giáo dục (3.3tr) | ✅ | ✅ Giáo dục |
| 418 | trả điện 860.000 sáng nay | Nhà ở (860k) | Nhà ở (860k) | ✅ | ✅ Nhà ở |
| 419 | tiền trọ 2.950.000 | Nhà ở (3.0tr) | Nhà ở (3.0tr) | ✅ | ✅ Nhà ở |
| 420 | chi bia 400 cành rồi son 2900 ngàn | Ăn uống (400k)<br>Mua sắm (2.9tr) | Ăn uống (400k)<br>Mua sắm (2.9tr) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 421 | đi chợ 2640 cành | Mua sắm (2.6tr) | Mua sắm (2.6tr) | ✅ | ✅ Mua sắm |
| 422 | thanh toán spotify 3620 cành | Giải trí (3.6tr) | Giải trí (4k) | ✅ | ✅ Giải trí |
| 423 | grab 700.000 | Đi lại (700k) | Đi lại (700k) | ✅ | ✅ Đi lại |
| 424 | 820 cành tiền nước muối | Y tế (820k) | Chưa xác định (8.2tr) | ❌ | ❌ Missed: Y tế<br>⚠️ Extra: Chưa xác định |
| 425 | hủ tiếu 230 ngàn | Ăn uống (230k) | Ăn uống (230k) | ✅ | ✅ Ăn uống |
| 426 | taxi 500k | Đi lại (500k) | Đi lại (500k) | ✅ | ✅ Đi lại |
| 427 | thu cf 80 cành rồi 2.630.000 tiền túi xách | Ăn uống (80k)<br>Mua sắm (2.6tr) | Chưa xác định (80k)<br>Mua sắm (2.6tr) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 428 | khau trang 830 ngan | Y tế (830k) | Mua sắm (830k) | ✅ | ✅ Y tế |
| 429 | 360 canh com tam | Ăn uống (360k) | Ăn uống (360k) | ✅ | ✅ Ăn uống |
| 430 | quần áo 2.7 triệu sau đó nhận xăng 800.000 trưa... | Mua sắm (2.7tr)<br>Đi lại (800k) | Mua sắm (2.7tr)<br>Chưa xác định (800.0tr) | ❌ | ✅ Mua sắm<br>❌ Missed: Đi lại<br>⚠️ Extra: Chưa xác định |
| 431 | điện 4.24m | Nhà ở (4.2tr) | Chưa xác định (4.2tr) | ✅ | ✅ Nhà ở |
| 432 | đi du lịch hết 3.24tr | Giải trí (3.2tr) | Giải trí (3.2tr) | ✅ | ✅ Giải trí |
| 433 | hủ tiếu 290000 cộng son 720k | Ăn uống (290k)<br>Mua sắm (720k) | Ăn uống (290k)<br>Mua sắm (720k) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 434 | tien cong 2.97m | Thu nhập (3.0tr) | Thu nhập (3.0tr) | ✅ | ✅ Thu nhập |
| 435 | di thuoc het 200 canh với sửa xe 1.210.000 | Y tế (200k)<br>Đi lại (1.2tr) | Y tế (20k)<br>Nhà ở (1.2tr) | ✅ | ✅ Y tế<br>✅ Đi lại |
| 436 | đi giày hết 1290k với 580000 karaoke cộng nhận ... | Mua sắm (1.3tr)<br>Giải trí (580k)<br>Giáo dục (390k) | Mua sắm (1.3tr)<br>Chưa xác định (580.0tr)<br>Giáo dục (390k) | ❌ | ✅ Mua sắm<br>❌ Missed: Giải trí<br>✅ Giáo dục<br>⚠️ Extra: Chưa xác định |
| 437 | karaoke 2030 cành rồi bowling 2130 ngàn với gas... | Giải trí (2.0tr)<br>Giải trí (2.1tr)<br>Nhà ở (4.2tr) | Giải trí (2.0tr)<br>Giải trí (2.1tr)<br>Đi lại (4.2tr) | ✅ | ✅ Giải trí<br>✅ Giải trí<br>✅ Nhà ở |
| 438 | 200.000 tiền tiền nhà sau đó đi xăng hết 169000... | Nhà ở (200k)<br>Đi lại (1.7tr)<br>Giải trí (4.2tr) | Nhà ở (200k)<br>Đi lại (1.7tr)<br>Giải trí (4k) | ✅ | ✅ Nhà ở<br>✅ Đi lại<br>✅ Giải trí |
| 439 | nhận vé xem phim 1.02m | Giải trí (1.0tr) | Giải trí (1.0tr) | ✅ | ✅ Giải trí |
| 440 | trả book vé 830000 | Giải trí (830k) | Chưa xác định (830k) | ✅ | ✅ Giải trí |
| 441 | đi khóa học online hết 3.06m | Giáo dục (3.1tr) | Giáo dục (3.1tr) | ✅ | ✅ Giáo dục |
| 442 | đòi nợ 11.070.000 | Thu nhập (11.1tr) | Thu nhập (11.1tr) | ✅ | ✅ Thu nhập |
| 443 | hoàn tiền 18.020.000 | Thu nhập (18.0tr) | Thu nhập (18.0tr) | ✅ | ✅ Thu nhập |
| 444 | chi karaoke 3.940.000 | Giải trí (3.9tr) | Giải trí (3.9tr) | ✅ | ✅ Giải trí |
| 445 | 3.29tr tien sach giao khoa, đi tiền công hết 59... | Giáo dục (3.3tr)<br>Thu nhập (5.9tr) | Chưa xác định (3.3tr)<br>Thu nhập (5.9tr) | ✅ | ✅ Giáo dục<br>✅ Thu nhập |
| 446 | 3730k sửa ống nước với đi vở hết 8.52m | Nhà ở (3.7tr)<br>Giáo dục (8.5tr) | Nhà ở (3.7tr)<br>Chưa xác định (8.5tr) | ✅ | ✅ Nhà ở<br>✅ Giáo dục |
| 447 | karaoke 1390k rồi 2350k tiền bóng đèn | Giải trí (1.4tr)<br>Nhà ở (2.4tr) | Giải trí (1.4tr)<br>Mua sắm (2.4tr) | ✅ | ✅ Giải trí<br>✅ Nhà ở |
| 448 | 4.200.000 bowling, bowling 3660 ngan | Giải trí (4.2tr)<br>Giải trí (3.7tr) | Chưa xác định (4.2tr)<br>Chưa xác định (3.7tr) | ✅ | ✅ Giải trí<br>✅ Giải trí |
| 449 | thu cơm tấm 140 cành chiều nay, đi hủ tiếu hết ... | Ăn uống (140k)<br>Ăn uống (30k)<br>Đi lại (1.2tr) | Ăn uống (140k)<br>Ăn uống (30k)<br>Nhà ở (1.2tr) | ✅ | ✅ Ăn uống<br>✅ Ăn uống<br>✅ Đi lại |
| 450 | kính thuốc 1280 ngàn. 4.21m internet cộng vở 5.... | Y tế (1.3tr)<br>Nhà ở (4.2tr)<br>Giáo dục (5.4tr) | Y tế (1.3tr)<br>Chưa xác định (4.2tr)<br>Giáo dục (5.4tr) | ✅ | ✅ Y tế<br>✅ Nhà ở<br>✅ Giáo dục |
| 451 | đóng tiền nhà 1300 cành | Nhà ở (1.3tr) | Nhà ở (13.0tr) | ✅ | ✅ Nhà ở |
| 452 | đi váy hết 1.89m | Mua sắm (1.9tr) | Mua sắm (1.9tr) | ✅ | ✅ Mua sắm |
| 453 | nhận cà phê 370000 hôm kia | Ăn uống (370k) | Thu nhập (370k) | ✅ | ✅ Ăn uống |
| 454 | but 1.580.000 | Giáo dục (1.6tr) | Chưa xác định (1.6tr) | ✅ | ✅ Giáo dục |
| 455 | vừa xem phim 1.97m - di tien nha het 1300k | Giải trí (2.0tr)<br>Nhà ở (1.3tr) | Giải trí (2.0tr)<br>Nhà ở (1.3tr) | ✅ | ✅ Giải trí<br>✅ Nhà ở |
| 456 | mới khám bệnh 1380 cành | Y tế (1.4tr) | Y tế (1.4tr) | ✅ | ✅ Y tế |
| 457 | 3.57 triệu tiền trọ sau đó mỹ phẩm 1850 ngàn | Nhà ở (3.6tr)<br>Mua sắm (1.9tr) | Nhà ở (3.6tr)<br>Mua sắm (1.9tr) | ✅ | ✅ Nhà ở<br>✅ Mua sắm |
| 458 | di kinh thuoc het 1.74 trieu - xem phim 4.570.0... | Y tế (1.7tr)<br>Giải trí (4.6tr)<br>Giáo dục (9.5tr) | Chưa xác định (1.7tr)<br>Giải trí (4.6tr)<br>Giáo dục (9.5tr) | ✅ | ✅ Y tế<br>✅ Giải trí<br>✅ Giáo dục |
| 459 | thanh toán vé xem phim 1750 ngàn lúc nãy | Giải trí (1.8tr) | Giải trí (1.8tr) | ✅ | ✅ Giải trí |
| 460 | đi sữa tắm hết 65 cành | Mua sắm (65k) | Chưa xác định (65k) | ✅ | ✅ Mua sắm |
| 461 | vừa dịch vụ chung cư 1.360.000 với 170 ngàn tiề... | Nhà ở (1.4tr)<br>Ăn uống (170k)<br>Giáo dục (6.5tr) | Nhà ở (1.4tr)<br>Ăn uống (170k)<br>Giáo dục (6.5tr) | ✅ | ✅ Nhà ở<br>✅ Ăn uống<br>✅ Giáo dục |
| 462 | 6370000 tiền photo tài liệu | Giáo dục (6.4tr) | Chưa xác định (6.4tr) | ✅ | ✅ Giáo dục |
| 463 | 4260 ngàn tiền dịch vụ chung cư sau đó nhận dụn... | Nhà ở (4.3tr)<br>Giáo dục (3.9tr)<br>Mua sắm (1.2tr) | Nhà ở (4.3tr)<br>Giáo dục (3.9tr)<br>Y tế (1.2tr) | ✅ | ✅ Nhà ở<br>✅ Giáo dục<br>✅ Mua sắm |
| 464 | lương 19410k | Thu nhập (19.4tr) | Thu nhập (19.4tr) | ✅ | ✅ Thu nhập |
| 465 | chi karaoke 4650000 sáng nay rồi vừa cafe 120k | Giải trí (4.7tr)<br>Ăn uống (120k) | Giải trí (4.7tr)<br>Ăn uống (120k) | ✅ | ✅ Giải trí<br>✅ Ăn uống |
| 466 | đi photo tài liệu hết 5160 ngàn | Giáo dục (5.2tr) | Chưa xác định (5.2tr) | ✅ | ✅ Giáo dục |
| 467 | mua vé máy bay 170 ngàn, 1070000 viện phí thêm ... | Đi lại (170k)<br>Y tế (1.1tr)<br>Y tế (1.0tr) | Mua sắm (170k)<br>Y tế (1.0tr) | ❌ | ✅ Đi lại<br>✅ Y tế<br>❌ Missed: Y tế |
| 468 | được cho 5150 ngàn cộng 210 cành vé xe | Thu nhập (5.2tr)<br>Đi lại (210k) | Thu nhập (5.2tr)<br>Đi lại (210k) | ✅ | ✅ Thu nhập<br>✅ Đi lại |
| 469 | đi toeic hết 3970 ngàn | Giáo dục (4.0tr) | Giáo dục (4.0tr) | ✅ | ✅ Giáo dục |
| 470 | đi xét nghiệm hết 220 cành | Y tế (220k) | Y tế (220k) | ✅ | ✅ Y tế |
| 471 | wifi 3670 cành - có thưởng 10900 ngàn | Nhà ở (3.7tr)<br>Thu nhập (10.9tr) | Chưa xác định (4k)<br>Chưa xác định (10.9tr) | ❌ | ❌ Missed: Nhà ở<br>✅ Thu nhập<br>⚠️ Extra: Chưa xác định |
| 472 | gửi xe 370000 - di khoa hoc online het 5010k | Đi lại (370k)<br>Giáo dục (5.0tr) | Đi lại (370k)<br>Giáo dục (5.0tr) | ✅ | ✅ Đi lại<br>✅ Giáo dục |
| 473 | đi cf hết 110000 với 2.06tr tiền sữa tắm | Ăn uống (110k)<br>Mua sắm (2.1tr) | Chưa xác định (110k)<br>Mua sắm (2.1tr) | ✅ | ✅ Ăn uống<br>✅ Mua sắm |
| 474 | hủ tiếu 200000 | Ăn uống (200k) | Ăn uống (200k) | ✅ | ✅ Ăn uống |
| 475 | 1.81m tiền bowling | Giải trí (1.8tr) | Giải trí (1.8tr) | ✅ | ✅ Giải trí |
| 476 | vừa điện 900.000 | Nhà ở (900k) | Chưa xác định (900k) | ✅ | ✅ Nhà ở |
| 477 | sách 2760000 | Mua sắm (2.8tr) | Mua sắm (2.8tr) | ✅ | ✅ Mua sắm |
| 478 | đi sách giáo khoa hết 7450000, bánh mì 220k | Giáo dục (7.5tr)<br>Ăn uống (220k) | Giáo dục (7.5tr)<br>Ăn uống (220k) | ✅ | ✅ Giáo dục<br>✅ Ăn uống |
| 479 | đi cafe hết 50k, bánh mì 250 cành | Ăn uống (50k)<br>Ăn uống (250k) | Ăn uống (50k)<br>Chưa xác định (0đ) | ❌ | ✅ Ăn uống<br>❌ Missed: Ăn uống<br>⚠️ Extra: Chưa xác định |
| 480 | bún bò 190.000 | Ăn uống (190k) | Ăn uống (190k) | ✅ | ✅ Ăn uống |
| 481 | bảo dưỡng xe 1.19tr | Đi lại (1.2tr) | Chưa xác định (1.2tr) | ✅ | ✅ Đi lại |
| 482 | đi nước hết 1.190.000 | Nhà ở (1.2tr) | Chưa xác định (1.2tr) | ✅ | ✅ Nhà ở |
| 483 | mua bowling 770 ngàn sau đó thanh toán bánh mì ... | Giải trí (770k)<br>Ăn uống (210k)<br>Y tế (35k) | Giải trí (770k)<br>Ăn uống (210k)<br>Y tế (35k) | ✅ | ✅ Giải trí<br>✅ Ăn uống<br>✅ Y tế |
| 484 | đi rau củ hết 2980000 | Mua sắm (3.0tr) | Mua sắm (3.0tr) | ✅ | ✅ Mua sắm |
| 485 | di sach giao khoa het 2.640.000 - đi tiền học h... | Giáo dục (2.6tr)<br>Giáo dục (4.6tr) | Giáo dục (2.6tr)<br>Giáo dục (4.6tr) | ✅ | ✅ Giáo dục<br>✅ Giáo dục |
| 486 | mua sinh tố 370k và sách giáo khoa 4.180.000 | Ăn uống (370k)<br>Giáo dục (4.2tr) | Ăn uống (370k)<br>Giáo dục (4.2tr) | ✅ | ✅ Ăn uống<br>✅ Giáo dục |
| 487 | đi gửi xe hết 710 cành | Đi lại (710k) | Đi lại (710k) | ✅ | ✅ Đi lại |
| 488 | đi lì xì hết 14440 cành | Thu nhập (14.4tr) | Chưa xác định (14k) | ❌ | ❌ Missed: Thu nhập<br>⚠️ Extra: Chưa xác định |
| 489 | khám bệnh 1580000 | Y tế (1.6tr) | Y tế (1.6tr) | ✅ | ✅ Y tế |
| 490 | 1.690.000 váy | Mua sắm (1.7tr) | Mua sắm (1.7tr) | ✅ | ✅ Mua sắm |
| 491 | thưởng 5.63 triệu | Thu nhập (5.6tr) | Thu nhập (5.6tr) | ✅ | ✅ Thu nhập |
| 492 | được đòi nợ 2.39tr thêm đi viện phí hết 1470 ngàn | Thu nhập (2.4tr)<br>Y tế (1.5tr) | Thu nhập (2.4tr)<br>Y tế (1.5tr) | ✅ | ✅ Thu nhập<br>✅ Y tế |
| 493 | 120000 banh mi với thanh toán phở 470000 | Ăn uống (120k)<br>Ăn uống (470k) | Ăn uống (120k)<br>Ăn uống (470k) | ✅ | ✅ Ăn uống<br>✅ Ăn uống |
| 494 | đi be hết 730.000 | Đi lại (730k) | Chưa xác định (730k) | ✅ | ✅ Đi lại |
| 495 | 1480k tiền khám bệnh | Y tế (1.5tr) | Y tế (1.5tr) | ✅ | ✅ Y tế |
| 496 | vừa vé xem phim 2440 ngàn | Giải trí (2.4tr) | Giải trí (2.4tr) | ✅ | ✅ Giải trí |
| 497 | 1.49tr khám bệnh | Y tế (1.5tr) | Chưa xác định (1.5tr) | ✅ | ✅ Y tế |
| 498 | thanh toán giày 2.38tr, tiền trọ 2.350.000 | Mua sắm (2.4tr)<br>Nhà ở (2.4tr) | Mua sắm (2.4tr)<br>Nhà ở (2.4tr) | ✅ | ✅ Mua sắm<br>✅ Nhà ở |
| 499 | tạp chí 500000 | Mua sắm (500k) | Giải trí (500k) | ✅ | ✅ Mua sắm |
| 500 | xét nghiệm 1.5m. đi phở hết 470k | Y tế (1.5tr)<br>Ăn uống (470k) | Y tế (1.5tr)<br>Ăn uống (470k) | ✅ | ✅ Y tế<br>✅ Ăn uống |
| 501 | 3.330.000 tiền xem phim | Giải trí (3.3tr) | Giải trí (3.3tr) | ✅ | ✅ Giải trí |
| 502 | cà phê 480 ngàn và đòi nợ 3710 cành cộng 2330k ... | Ăn uống (480k)<br>Thu nhập (3.7tr)<br>Mua sắm (2.3tr) | Ăn uống (480k)<br>Chưa xác định (0đ)<br>Mua sắm (2.3tr) | ❌ | ✅ Ăn uống<br>❌ Missed: Thu nhập<br>✅ Mua sắm<br>⚠️ Extra: Chưa xác định |
| 503 | đi gas hết 2440k | Nhà ở (2.4tr) | Chưa xác định (2.4tr) | ✅ | ✅ Nhà ở |
| 504 | thu giày 1.85m, bảo dưỡng xe 860 cành | Mua sắm (1.9tr)<br>Đi lại (860k) | Mua sắm (1.9tr)<br>Đi lại (860k) | ✅ | ✅ Mua sắm<br>✅ Đi lại |
| 505 | vừa phở 110 cành | Ăn uống (110k) | Ăn uống (110k) | ✅ | ✅ Ăn uống |
| 506 | thanh toán điện 2490k chiều nay | Nhà ở (2.5tr) | Nhà ở (2.5tr) | ✅ | ✅ Nhà ở |
| 507 | đi khám bệnh hết 1650 cành | Y tế (1.6tr) | Y tế (1.6tr) | ✅ | ✅ Y tế |
| 508 | moi tien tro 760 canh - đóng dầu gội 1.960.000 | Nhà ở (760k)<br>Mua sắm (2.0tr) | Chưa xác định (760k)<br>Mua sắm (2.0tr) | ✅ | ✅ Nhà ở<br>✅ Mua sắm |
| 509 | xet nghiem 1.000.000 | Y tế (1.0tr) | Chưa xác định (1.0tr) | ✅ | ✅ Y tế |
| 510 | 1030000 giày | Mua sắm (1.0tr) | Mua sắm (1.0tr) | ✅ | ✅ Mua sắm |

---

## 🔍 Bảng 4: Phân Tích Lỗi Chi Tiết

**Tổng số mẫu lỗi:** 39

### 📌 Mẫu #1

**Input:** `di rua xe het 1930k cộng 330 cành bus`

**Latency:** 101404ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Đi lại | 1.9tr | Chi phí |
| 2 | Đi lại | 330k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 1.9tr | Chi phí |
| 2 | Đi lại | 330k | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Đi lại (1.9tr) → Đi lại (330k)
- ❌ **BỎ SÓT:** Kỳ vọng `Đi lại (330k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (1.9tr)` không có trong kỳ vọng

---

### 📌 Mẫu #7

**Input:** `9470 canh hoan tien`

**Latency:** 47934ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 9.5tr | Thu nhập |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 9k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Thu nhập (9.5tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (9k)` không có trong kỳ vọng

---

### 📌 Mẫu #11

**Input:** `lì xì 5490k thêm 890 ngàn vé máy bay`

**Latency:** 87770ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 5.5tr | Thu nhập |
| 2 | Đi lại | 890k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 5.5tr | Thu nhập |
| 2 | Chưa xác định | 890k | Chi phí |
| 3 | Chưa xác định | 0đ | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Thu nhập (5.5tr) → Chưa xác định (5.5tr)
- ✅ **ĐÚNG:** Đi lại (890k) → Chưa xác định (890k)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #14

**Input:** `1620 cành điện`

**Latency:** 46800ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 1.6tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 0đ | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (1.6tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #16

**Input:** `đi lì xì hết 10640 cành với đi khám bệnh hết 790.000`

**Latency:** 73987ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 10.6tr | Thu nhập |
| 2 | Y tế | 790k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 11k | Chi phí |
| 2 | Y tế | 790k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Thu nhập (10.6tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Y tế (790k) → Y tế (790k)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (11k)` không có trong kỳ vọng

---

### 📌 Mẫu #37

**Input:** `lương thưởng 3280k`

**Latency:** 75463ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 3.3tr | Thu nhập |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 3.3tr | Thu nhập |
| 2 | Chưa xác định | 0đ | Thu nhập |

**Phân tích matching:**
- ✅ **ĐÚNG:** Thu nhập (3.3tr) → Thu nhập (3.3tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #56

**Input:** `2020000 đòi nợ`

**Latency:** 53535ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 2.0tr | Thu nhập |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 2.0tr | Thu nhập |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Thu nhập (2.0tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (2.0tr)` không có trong kỳ vọng

---

### 📌 Mẫu #61

**Input:** `netflix 470.000, nhậu 35 cành với 480 ngàn tiền be`

**Latency:** 71557ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 470k | Chi phí |
| 2 | Ăn uống | 35k | Chi phí |
| 3 | Đi lại | 480k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 470k | Chi phí |
| 2 | Ăn uống | 480k | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Giải trí (470k) → Giải trí (470k)
- ✅ **ĐÚNG:** Ăn uống (35k) → Ăn uống (480k)
- ❌ **BỎ SÓT:** Kỳ vọng `Đi lại (480k)` nhưng không tìm thấy

---

### 📌 Mẫu #79

**Input:** `dong my pham 240k chieu nay và mỹ phẩm 2000 cành - bảo dưỡng xe 1450 ngàn`

**Latency:** 95787ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 240k | Chi phí |
| 2 | Mua sắm | 2.0tr | Chi phí |
| 3 | Đi lại | 1.4tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 240k | Chi phí |
| 2 | Mua sắm | 2k | Chi phí |
| 3 | Nhà ở | 1.4tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Mua sắm (240k) → Mua sắm (2k)
- ❌ **BỎ SÓT:** Kỳ vọng `Mua sắm (2.0tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Đi lại (1.4tr) → Nhà ở (1.4tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (240k)` không có trong kỳ vọng

---

### 📌 Mẫu #105

**Input:** `di internet het 3600 ngan và đi chợ 680.000`

**Latency:** 74784ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 3.6tr | Chi phí |
| 2 | Mua sắm | 680k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 360k | Chi phí |
| 2 | Mua sắm | 680k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (3.6tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Mua sắm (680k) → Mua sắm (680k)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (360k)` không có trong kỳ vọng

---

### 📌 Mẫu #110

**Input:** `nhận túi xách 240 cành`

**Latency:** 44776ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 240k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 2.4tr | Thu nhập |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Mua sắm (240k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (2.4tr)` không có trong kỳ vọng

---

### 📌 Mẫu #113

**Input:** `nước muối 710000 rồi 45 cành cà phê`

**Latency:** 75183ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Y tế | 710k | Chi phí |
| 2 | Ăn uống | 45k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 710k | Chi phí |
| 2 | Chưa xác định | 0đ | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Y tế (710k) → Chưa xác định (710k)
- ❌ **BỎ SÓT:** Kỳ vọng `Ăn uống (45k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #119

**Input:** `du lịch 3890 cành`

**Latency:** 45901ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 3.9tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 4k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Giải trí (3.9tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (4k)` không có trong kỳ vọng

---

### 📌 Mẫu #125

**Input:** `730 cành kính thuốc`

**Latency:** 55287ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Y tế | 730k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 7.3tr | Chi phí |
| 2 | Y tế | 100k | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Y tế (730k) → Y tế (100k)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (7.3tr)` không có trong kỳ vọng

---

### 📌 Mẫu #128

**Input:** `2370000 karaoke, rửa xe 890 ngàn`

**Latency:** 71722ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 2.4tr | Chi phí |
| 2 | Đi lại | 890k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 2370.0tr | Chi phí |
| 2 | Chưa xác định | 890k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Giải trí (2.4tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Đi lại (890k) → Chưa xác định (890k)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (2370.0tr)` không có trong kỳ vọng

---

### 📌 Mẫu #178

**Input:** `son 1.98m`

**Latency:** 35206ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 2.0tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | { "nội dung": "Son cao 1.98m ư?", "số tiền": "98đ"} | 98đ | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Mua sắm (2.0tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `{ "nội dung": "Son cao 1.98m ư?", "số tiền": "98đ"} (98đ)` không có trong kỳ vọng

---

### 📌 Mẫu #183

**Input:** `rác 4140 cành`

**Latency:** 44536ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 4.1tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 4k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (4.1tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (4k)` không có trong kỳ vọng

---

### 📌 Mẫu #193

**Input:** `toeic 95 cành`

**Latency:** 45496ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giáo dục | 95k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 950k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Giáo dục (95k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (950k)` không có trong kỳ vọng

---

### 📌 Mẫu #208

**Input:** `vừa dụng cụ học tập 7.32m trưa nay`

**Latency:** 74242ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giáo dục | 7.3tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giáo dục | 7.3tr | Chi phí |
| 2 | Chưa xác định | 0đ | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Giáo dục (7.3tr) → Giáo dục (7.3tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #224

**Input:** `my pham 2.620.000. đi mỹ phẩm hết 330k với đi kính thuốc hết 1110k`

**Latency:** 95114ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 2.6tr | Chi phí |
| 2 | Mua sắm | 330k | Chi phí |
| 3 | Y tế | 1.1tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 2.6tr | Thu nhập |
| 2 | Mua sắm | 330k | Chi phí |
| 3 | Y tế | 1.1tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Mua sắm (2.6tr) → Mua sắm (330k)
- ❌ **BỎ SÓT:** Kỳ vọng `Mua sắm (330k)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Y tế (1.1tr) → Y tế (1.1tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (2.6tr)` không có trong kỳ vọng

---

### 📌 Mẫu #248

**Input:** `nhận internet 4460 cành`

**Latency:** 45730ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 4.5tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 4k | Thu nhập |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (4.5tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (4k)` không có trong kỳ vọng

---

### 📌 Mẫu #294

**Input:** `đi xem phim hết 4.010.000 sau đó đi gas hết 4270 ngàn, điện 360k`

**Latency:** 97582ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 4.0tr | Chi phí |
| 2 | Nhà ở | 4.3tr | Chi phí |
| 3 | Nhà ở | 360k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 4.0tr | Chi phí |
| 2 | Đi lại | 4.3tr | Chi phí |
| 3 | Nhà ở | 360k | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Giải trí (4.0tr) → Giải trí (4.0tr)
- ✅ **ĐÚNG:** Nhà ở (4.3tr) → Nhà ở (360k)
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (360k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Đi lại (4.3tr)` không có trong kỳ vọng

---

### 📌 Mẫu #325

**Input:** `be 1730 cành sau đó đi be hết 880.000 với 2880000 giày`

**Latency:** 103250ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Đi lại | 1.7tr | Chi phí |
| 2 | Đi lại | 880k | Chi phí |
| 3 | Mua sắm | 2.9tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 2k | Chi phí |
| 2 | Chưa xác định | 880k | Chi phí |
| 3 | Mua sắm | 2.9tr | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Đi lại (1.7tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Đi lại (880k) → Chưa xác định (880k)
- ✅ **ĐÚNG:** Mua sắm (2.9tr) → Mua sắm (2.9tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (2k)` không có trong kỳ vọng

---

### 📌 Mẫu #338

**Input:** `thanh toán game 4050 cành hôm kia`

**Latency:** 44282ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Giải trí | 4.0tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 4k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Giải trí (4.0tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (4k)` không có trong kỳ vọng

---

### 📌 Mẫu #341

**Input:** `mua nước 3920 cành tối qua`

**Latency:** 48423ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 3.9tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Ăn uống | 4k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (3.9tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Ăn uống (4k)` không có trong kỳ vọng

---

### 📌 Mẫu #343

**Input:** `1430000 dầu gội rồi viện phí 1960k`

**Latency:** 85668ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 1.4tr | Chi phí |
| 2 | Y tế | 2.0tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 1.4tr | Chi phí |
| 2 | Chưa xác định | 0đ | Chi phí |
| 3 | Y tế | 2.0tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Mua sắm (1.4tr) → Chưa xác định (1.4tr)
- ✅ **ĐÚNG:** Y tế (2.0tr) → Y tế (2.0tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #353

**Input:** `đi bán đồ cũ hết 19680 cành - đi gojek hết 1550 ngàn`

**Latency:** 79063ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 19.7tr | Thu nhập |
| 2 | Đi lại | 1.6tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 20k | Chi phí |
| 2 | Đi lại | 1.6tr | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Thu nhập (19.7tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Đi lại (1.6tr) → Đi lại (1.6tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (20k)` không có trong kỳ vọng

---

### 📌 Mẫu #366

**Input:** `thu đi chợ 1220000. 1.630.000 ao thun`

**Latency:** 73094ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 1.2tr | Chi phí |
| 2 | Mua sắm | 1.6tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 1.2tr | Chi phí |
| 2 | Mua sắm | 1.6tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Mua sắm (1.2tr) → Mua sắm (1.6tr)
- ❌ **BỎ SÓT:** Kỳ vọng `Mua sắm (1.6tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (1.2tr)` không có trong kỳ vọng

---

### 📌 Mẫu #369

**Input:** `di khau trang het 1440 canh`

**Latency:** 50868ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Y tế | 1.4tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 14.4tr | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Y tế (1.4tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (14.4tr)` không có trong kỳ vọng

---

### 📌 Mẫu #394

**Input:** `1230 canh tien xe om`

**Latency:** 74822ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Đi lại | 1.2tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 1.2tr | Thu nhập |
| 2 | Chưa xác định | 0đ | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Đi lại (1.2tr) → Chưa xác định (1.2tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #409

**Input:** `mua gas 2480 cành`

**Latency:** 54225ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 2.5tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 2k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (2.5tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (2k)` không có trong kỳ vọng

---

### 📌 Mẫu #424

**Input:** `820 cành tiền nước muối`

**Latency:** 57252ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Y tế | 820k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 8.2tr | Thu nhập |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Y tế (820k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (8.2tr)` không có trong kỳ vọng

---

### 📌 Mẫu #430

**Input:** `quần áo 2.7 triệu sau đó nhận xăng 800.000 trưa nay`

**Latency:** 76451ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 2.7tr | Chi phí |
| 2 | Đi lại | 800k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 2.7tr | Chi phí |
| 2 | Chưa xác định | 800.0tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Mua sắm (2.7tr) → Mua sắm (2.7tr)
- ❌ **BỎ SÓT:** Kỳ vọng `Đi lại (800k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (800.0tr)` không có trong kỳ vọng

---

### 📌 Mẫu #436

**Input:** `đi giày hết 1290k với 580000 karaoke cộng nhận khóa học online 390 ngàn`

**Latency:** 105561ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 1.3tr | Chi phí |
| 2 | Giải trí | 580k | Chi phí |
| 3 | Giáo dục | 390k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 1.3tr | Chi phí |
| 2 | Chưa xác định | 580.0tr | Chi phí |
| 3 | Giáo dục | 390k | Thu nhập |

**Phân tích matching:**
- ✅ **ĐÚNG:** Mua sắm (1.3tr) → Mua sắm (1.3tr)
- ❌ **BỎ SÓT:** Kỳ vọng `Giải trí (580k)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Giáo dục (390k) → Giáo dục (390k)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (580.0tr)` không có trong kỳ vọng

---

### 📌 Mẫu #467

**Input:** `mua vé máy bay 170 ngàn, 1070000 viện phí thêm đi xét nghiệm hết 1.01tr`

**Latency:** 77528ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Đi lại | 170k | Chi phí |
| 2 | Y tế | 1.1tr | Chi phí |
| 3 | Y tế | 1.0tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Mua sắm | 170k | Chi phí |
| 2 | Y tế | 1.0tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Đi lại (170k) → Mua sắm (170k)
- ✅ **ĐÚNG:** Y tế (1.1tr) → Y tế (1.0tr)
- ❌ **BỎ SÓT:** Kỳ vọng `Y tế (1.0tr)` nhưng không tìm thấy

---

### 📌 Mẫu #471

**Input:** `wifi 3670 cành - có thưởng 10900 ngàn`

**Latency:** 58776ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Nhà ở | 3.7tr | Chi phí |
| 2 | Thu nhập | 10.9tr | Thu nhập |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 4k | Chi phí |
| 2 | Chưa xác định | 10.9tr | Thu nhập |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Nhà ở (3.7tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Thu nhập (10.9tr) → Chưa xác định (10.9tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (4k)` không có trong kỳ vọng

---

### 📌 Mẫu #479

**Input:** `đi cafe hết 50k, bánh mì 250 cành`

**Latency:** 74500ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Ăn uống | 50k | Chi phí |
| 2 | Ăn uống | 250k | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Ăn uống | 50k | Chi phí |
| 2 | Chưa xác định | 0đ | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Ăn uống (50k) → Ăn uống (50k)
- ❌ **BỎ SÓT:** Kỳ vọng `Ăn uống (250k)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

### 📌 Mẫu #488

**Input:** `đi lì xì hết 14440 cành`

**Latency:** 49006ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Thu nhập | 14.4tr | Thu nhập |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Chưa xác định | 14k | Chi phí |

**Phân tích matching:**
- ❌ **BỎ SÓT:** Kỳ vọng `Thu nhập (14.4tr)` nhưng không tìm thấy
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (14k)` không có trong kỳ vọng

---

### 📌 Mẫu #502

**Input:** `cà phê 480 ngàn và đòi nợ 3710 cành cộng 2330k rau củ`

**Latency:** 100755ms

**Expected (Kỳ vọng):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Ăn uống | 480k | Chi phí |
| 2 | Thu nhập | 3.7tr | Thu nhập |
| 3 | Mua sắm | 2.3tr | Chi phí |

**Predicted (Dự đoán):**
| # | Danh mục | Số tiền | Loại |
|---|----------|---------|------|
| 1 | Ăn uống | 480k | Chi phí |
| 2 | Chưa xác định | 0đ | Thu nhập |
| 3 | Mua sắm | 2.3tr | Chi phí |

**Phân tích matching:**
- ✅ **ĐÚNG:** Ăn uống (480k) → Ăn uống (480k)
- ❌ **BỎ SÓT:** Kỳ vọng `Thu nhập (3.7tr)` nhưng không tìm thấy
- ✅ **ĐÚNG:** Mua sắm (2.3tr) → Mua sắm (2.3tr)
- ⚠️ **DƯ THỪA:** Dự đoán thêm `Chưa xác định (0đ)` không có trong kỳ vọng

---

## 📌 Ghi Chú

- **TP (True Positive):** Dự đoán đúng danh mục
- **FP (False Positive):** Dự đoán thêm giao dịch không có trong kỳ vọng
- **FN (False Negative):** Bỏ sót giao dịch có trong kỳ vọng
- **Perfect Match:** Tất cả giao dịch trong input đều được dự đoán đúng, không thiếu không thừa

---
*Báo cáo được tạo tự động bởi hệ thống đánh giá AI*
