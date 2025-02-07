# string : data ?
def encode(data):
    # This program encodes data
    # result be like : [Mode Indicator] + [Count Indicator] + [Encoded Data]

    # 5-L needs 108 bytes, 864 bits
    LEN = 108*8

    # 1. Byte Mode's Indicator : 0100
    mode_indicator = "0100"

    # 2. Count Indicator
        # a. convert length into binary
        # b. Version 5 needs 8 bit of Count Indicator, pad with prefix 0 
    # data = input()
    length = len(data)
    count_indicator = bin(length)[2:]
    count_indicator = (8-len(count_indicator))*'0' + count_indicator
    # print(length, count_indicator)

    # 3. Encode Data
    encoded_text = data.encode("iso-8859-1")

    # binary_string = " ".join(format(byte, '08b') for byte in encoded_text)
    # print(binary_string)
    binary_string = "".join(format(byte, '08b') for byte in encoded_text)
    # print(binary_string)

    result = mode_indicator + count_indicator + binary_string
    # print(result)

    # Terminator 0s
    result += '0' * min(4, LEN-len(result))
    # print(result, len)

    # fill 0s to reach 8 multiplers
    if len(result)%8 != 0:
        result += '0' * ( 8 - len(result) )
        
    # print(len(result), result) 

    # Pad Bytes
    A = "11101100"
    B = "00010001"
    while len(result) < LEN:
        result += A
        A, B = B, A

    # result = " ".join(result[i*8:(i+1)*8] for i in range(int(len(result)/8)))
    result = [ result[i*8:(i+1)*8] for i in range(int(len(result)/8)) ]

    # print(len(result), result)
    return result
