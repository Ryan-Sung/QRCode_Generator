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


# INIT ------

N, M = 37, 37
img = Image.new(mode='RGB', size=(N, M))
pixels = img.load()

color = [(255, 255, 255), (0, 0, 0)] # color[0] = white, color[1] = black
used = []

for i in range(N):
    for j in range(M):
        pixels[i, j] = (125, 125, 125)


# -----

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
        pixels[i, j] = color[FINDER[i][j]]
        pixels[i, M-7+j] = color[FINDER[i][j]]
        pixels[N-7+i, j] = color[FINDER[i][j]]
        
        used.append((i, j))
        used.append((i, M-7+j))
        used.append((N-7+i, j))

# print("FINDER", len(used))

# Step 2: Add the Separators
'''
for t in range(8):
    # horizontal
    pixels[t, 7] = color[0]
    pixels[N-t-1, 7] = color[0]
    pixels[t, M-7-1] = color[0]
    
    # vertical
    pixels[7, t] = color[0]
    pixels[7, M-t-1] = color[0]
    pixels[N-7-1, t] = color[0]
    
    used.append((t, 7))
    used.append((N-t-1, 7))
    used.append((t, M-7-1))
    used.append((7, t))
    used.append((7, M-t-1))
    used.append((N-7-1, t))
 '''   
for t in range(8):
    # horizontal
    pixels[t, 7] = color[0]
    pixels[N-t-1, 7] = color[0]
    pixels[t, M-7-1] = color[0]
    
    
    used.append((t, 7))
    used.append((N-t-1, 7))
    used.append((t, M-7-1))
    
# 會重複一格，所以這裡是 7
for t in range(7):
    # vertical
    pixels[7, t] = color[0]
    pixels[7, M-t-1] = color[0]
    pixels[N-7-1, t] = color[0]
    
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
        pixels[i+28, j+28] = color[ALIGNMENT[i][j]]
        
        used.append((i+28, j+28))



# Step 4: Add the Timing Patterns
for t in range(8, N-9+1):
    pixels[6, t] = color[~t&1]
    pixels[t, 6] = color[~t&1]
    
    used.append((6, t))
    used.append((t, 6))


# Step 5: Add the Dark Module and Reserved Areas
pixels[8, M-8] = color[1]
used.append((8, M-8))

# pixel[8, 8] 讓直的去放
format_pos = [ [(8, M-1), (8, M-2), (8, M-3), (8, M-4), (8, M-5), (8, M-6), (8, M-7), (8, 8), (8, 7), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0)],
               [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (7, 8), (N-8, 8), (N-7, 8), (N-6, 8), (N-5, 8), (N-4, 8), (N-3, 8), (N-2, 8), (N-1, 8)] ]
format_clr = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0]

for t in range(15):
    # pixels[format_pos[0][t]] = (0, 0, 255)
    # pixels[format_pos[1][t]] = (0, 0, 255)
    pixels[format_pos[0][t]] = color[format_clr[t]]
    pixels[format_pos[1][t]] = color[format_clr[t]]
    
    used.append(format_pos[0][t])
    used.append(format_pos[1][t])

def fill(data):
    data += '0' * 100 # for not used area
    
    idx = 0
    dy = -1
    
    a = (N-1, M-1)
    b = (N-2, M-1)
    
    while 1:
        if a not in used:
            pixels[a] = color[int(data[idx])]
            idx+=1
        if b not in used:
            pixels[b] = color[int(data[idx])]
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
            
        
    a = (5, 9)
    b = (4, 9)
    dy = 1
    
    while 1:
        print(a, b)
        if a not in used:
            pixels[a] = color[int(data[idx])]
            idx+=1
        if b not in used:
            pixels[b] = color[int(data[idx])]
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
            
            
def mask():
    # use mask 0
    # if (row + column) mod 2 == 0 -> change
    for i in range(N):
        for j in range(M):
            if  (i, j) not in used and (i+j) % 2 == 0:
                x = pixels[i, j][0]
                pixels[i, j] = (255-x, 255-x, 255-x)

def show():
    img.save('qrcode.jpg')
    img.show()

pixels[7, 9] = (0, 100, 100)
# show()
