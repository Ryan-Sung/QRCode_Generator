# Error Correcting Code.py
import reedsolo

# error correction code
def ecc(data):
    # 設定 RS 編碼的錯誤修正能力（這裡設定為 26 個糾錯碼字）
    rs = reedsolo.RSCodec(26)

    # === 1. 原始數據 ===
    # data = bytearray([32, 91, 11, 120, 209, 114, 220, 77, 67, 64, 236, 17, 236, 17, 236, 17])  # 原始數據碼字
    data = [int(x, 2) for x in data]
    # print("\u539f\u59cb\u6578\u64da:", list(data))

    # === 2. 產生 RS 編碼 ===
    encoded = rs.encode(data)  # 會自動附加 26 個 RS 校正碼字
    # print(list(encoded))
    return list(encoded)

