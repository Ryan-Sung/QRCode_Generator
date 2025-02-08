# version 5 = 37x37
'''
- Cite from thonky.com
Step 1: Add the Finder Patterns
Step 2: Add the Separators
Step 3: Add the Alignment Patterns
Step 4: Add the Timing Patterns
Step 5: Add the Dark Module and Reserved Areas
Step 6: Place the Data Bits
Next: Data Masking
'''

from PIL import Image
import copy

# INIT ------

N, M = 37, 37

WHITE, BLACK, NULL = 0, 1, 2
arr = [[NULL for j in range(M)] for i in range(N)]
color = [(255, 255, 255), (0, 0, 0), (125, 125, 125)] # color[0] = white, color[1] = black, color[2] = gray
used = []

for i in range(N):
    for j in range(M):
        arr[i][j] = NULL


# -----
# base graph area

# Step 1: Add the Finder Patterns
FINDER = [ [1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1]]

for i in range(7):
    for j in range(7):
        arr[i][j] = FINDER[i][j]
        arr[i][M-7+j] = FINDER[i][j]
        arr[N-7+i][j] = FINDER[i][j]
        
        used.append((i, j))
        used.append((i, M-7+j))
        used.append((N-7+i, j))

# Step 2: Add the Separators
for t in range(8):
    # horizontal
    arr[t][7] = WHITE
    arr[N-t-1][7] = WHITE
    arr[t][M-7-1] = WHITE
    
    used.append((t, 7))
    used.append((N-t-1, 7))
    used.append((t, M-7-1))
    
# 會重複一格，所以這裡是 7
for t in range(7):
    # vertical
    arr[7][t] = WHITE
    arr[7][M-t-1] = WHITE
    arr[N-7-1][t] = WHITE
    
    used.append((7, t))
    used.append((7, M-t-1))
    used.append((N-7-1, t))
    

# Step 3: Add the Alignment Patterns
ALIGNMENT = [ [1, 1, 1, 1, 1],
              [1, 0, 0, 0, 1],
              [1, 0, 1, 0, 1],
              [1, 0, 0, 0, 1],
              [1, 1, 1, 1, 1] ]

for i in range(5):
    for j in range(5):
        arr[i+28][j+28] = ALIGNMENT[i][j]
        
        used.append((i+28, j+28))



# Step 4: Add the Timing Patterns
for t in range(8, N-9+1):
    arr[6][t] = ~t&1
    arr[t][6] = ~t&1
    
    used.append((6, t))
    used.append((t, 6))


# Step 5: Add the Dark Module and Reserved Areas
arr[8][M-8] = 1
used.append((8, M-8))

# pixel[8, 8] 讓直的去放
format_pos = [ [(8, M-1), (8, M-2), (8, M-3), (8, M-4), (8, M-5), (8, M-6), (8, M-7), (8, 8), (8, 7), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0)],
               [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (7, 8), (N-8, 8), (N-7, 8), (N-6, 8), (N-5, 8), (N-4, 8), (N-3, 8), (N-2, 8), (N-1, 8)] ]

for t in range(15):
    used.append(format_pos[0][t])
    used.append(format_pos[1][t])
    
# ---------
# function area    
    
def fill(data):
    # 分兩塊做
    # 直到 vertical timing pattern 前一塊
    # 其後一塊
    
    data += '0' * 100 # for not used area
    
    idx = 0
    
    # 第一塊
    a = (N-1, M-1)
    b = (N-2, M-1)
    dy = -1
    
    while 1:
        if a not in used:
            arr[a[0]][a[1]] = int(data[idx])
            idx+=1
        if b not in used:
            arr[b[0]][b[1]] = int(data[idx])
            idx+=1
        
        a = (a[0], a[1] + dy)
        b = (b[0], b[1] + dy)
        
        if a == (7, 8) or b == (7, 8):
            break
        
        if a[1] < 0:
            a = (a[0]-2, 0)
            b = (b[0]-2, 0)
            dy = 1
            
        if a[1] == M:
            a = (a[0]-2, M-1)
            b = (b[0]-2, M-1)
            dy = -1
            
        
    # 第二塊
    a = (5, 9)
    b = (4, 9)
    dy = 1
    
    while 1:
        print(a, b)
        if a not in used:
            arr[a[0]][a[1]] = int(data[idx])
            idx+=1
        if b not in used:
            arr[b[0]][b[1]] = int(data[idx])
            idx+=1
        
        a = (a[0], a[1] + dy)
        b = (b[0], b[1] + dy)
        
        if a == (0, N-8) or b == (0, N-8):
            break
        
        if a[1] < 0:
            a = (a[0]-2, 0)
            b = (b[0]-2, 0)
            dy = 1
            
        if a[1] == M:
            a = (a[0]-2, M-1)
            b = (b[0]-2, M-1)
            dy = -1
        
def mask_n_format_n_finish():
    import eval # eval.py
    
    condition = [lambda x, y : (x+y)%2 == 0,
                 lambda x, y : y%2 == 0,
                 lambda x, y : x%3 == 0,
                 lambda x, y : (x+y)%3 == 0,
                 lambda x, y : (int(y/2) + int(x/3))%2 == 0,
                 lambda x, y : ( (x*y)%2 + (x*y)%3 ) == 0,
                 lambda x, y : ( (x*y)%2 + (x*y)%3 )%2 == 0,
                 lambda x, y : ( (x+y)%2 + (x*y)%3 )%2 == 0
                 ]
    
    format_pos = [ [(8, M-1), (8, M-2), (8, M-3), (8, M-4), (8, M-5), (8, M-6), (8, M-7), (8, 8), (8, 7), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0)],
                   [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (7, 8), (N-8, 8), (N-7, 8), (N-6, 8), (N-5, 8), (N-4, 8), (N-3, 8), (N-2, 8), (N-1, 8)] ]

    format_clr = [ [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                   [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
                   [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0] ]
    
    score = [eval.evaluate(copy.deepcopy(arr), used, condition[i]) for i in range(8)]
    print(score)
    
    tar = 0
    for i in range(8):
        if score[i] < score[tar]:
            tar = i
            
    # tar = 0
    for t in range(15):
        arr[ format_pos[0][t][0] ][ format_pos[0][t][1] ] = format_clr[tar][t]
        arr[ format_pos[1][t][0] ][ format_pos[1][t][1] ] = format_clr[tar][t]
   

    print("TAR :", tar)
    for i in range(N):
        for j in range(M):
            if  (i, j) not in used and condition[tar](i, j):
                arr[i][j] = 1 - arr[i][j]
                
def show_n_save(width):
    img = Image.new(mode='RGB', size=(N*width, M*width))
    pixels = img.load()

    for i in range(N):
        for j in range(M):
            for x in range(width):
                for y in range(width):
                    pixels[i*width+x, j*width+y] = (255, 255, 255) if arr[i][j] == 0 else (0, 0, 0)
                    
    img.save('qrcode.jpg')
    img.show()
