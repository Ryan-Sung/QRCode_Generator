import encode # encode.py
import ECC # error correction code
import construct # construct.py

INPUT = input()

encoded_data = encode.encode(INPUT)

final = ECC.ecc(encoded_data)

final = "".join(format(x, "08b") for x in final)

construct.fill(final)
construct.mask()
construct.show()