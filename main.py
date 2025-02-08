import encode # encode.py
import ECC # error correction code
import construct # construct.py
import eval # eval.py
import copy

import sys
INPUT = sys.stdin.read()  # 讀取標準輸入直到 EOF（Ctrl+D / Ctrl+Z）

encoded_data = encode.encode(INPUT)

final = ECC.ecc(encoded_data)

final = "".join(format(x, "08b") for x in final)

construct.fill(final)
construct.mask_n_format_n_finish()
construct.show_n_save(10) # width per module