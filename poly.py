MOD = 285

log_table = {}
antilog_table = {}
log_table[-1] = 0
antilog_table[0] = -1
x = 1
for i in range(256):
    log_table[i] = x
    antilog_table[x] = i
    x = (x*2)
    if x > 255:
        x ^= MOD
    

# ----------------

from itertools import repeat
    
# make coefficient presented by a^k
poly = []
poly.append([0])
poly.append([0, 0]) # (a^0)x - (a^0)1

for i in range(2, 100):
    poly.append( list(repeat(-1, i+1)) )
    exp = i-1
    # times x - a^(i-1)
    
    for j in range(1, i+1):
        poly[i][j] = poly[i-1][j-1]
    for j in range(i):
        coef = (log_table[poly[i][j]] ^ log_table[ (exp+poly[i-1][j])%255])
        print(i, j, '  ', poly[i][j], exp, '  ', coef)
        poly[i][j] = antilog_table[coef]
        

for i in range(100):
    print(poly[i])
