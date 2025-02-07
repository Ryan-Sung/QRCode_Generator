import reedsolo

# 設定 RS 編碼的錯誤修正能力（這裡設定為 26 個糾錯碼字）
rs = reedsolo.RSCodec(26)

# === 1. 原始數據 ===
data = bytearray([32, 91, 11, 120, 209, 114, 220, 77, 67, 64, 236, 17, 236, 17, 236, 17])  # 原始數據碼字
print("\u539f\u59cb\u6578\u64da:", list(data))

# === 2. 產生 RS 編碼 ===
encoded = rs.encode(data)  # 會自動附加 26 個 RS 校正碼字
print("\u7de8\u78bc\u5f8c\u6578\u64da:", list(encoded))  

# === 3. 模擬數據損壞 ===
corrupted = bytearray(encoded)
corrupted[1] = 0    # 第 2 個碼字損壞
corrupted[4] = 255  # 第 5 個碼字損壞
print("\u640d\u58de\u5f8c\u6578\u64da:", list(corrupted))

# === 4. 解碼並修復數據 ===
try:
    decoded = rs.decode(corrupted)  # 嘗試修正數據
    print("\u89e3\u78bc\u4e26\u4fee\u5fa9\u5f8c:", list(decoded))
except reedsolo.ReedSolomonError as e:
    print("\u89e3\u78bc\u5931\u6557:", e)
