MOD = 285

log_table = {}

x = 1
for i in range(256):
    log_table[i] = x
    x = (x*2)
    if x > 255:
        x ^= MOD
        
for i in range(256):
    print(i, log_table[i])