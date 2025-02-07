# Error Correcting Code.py
import reedsolo

# error correction code
def ecc(data):
    # 設定 RS 編碼的錯誤修正能力（這裡設定為 26 個糾錯碼字）
    rs = reedsolo.RSCodec(26)

    data = [int(x, 2) for x in data]
    encoded = rs.encode(data)
    
    return list(encoded)

