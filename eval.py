def cond_A(arr):
    cnt = 0
    N, M = len(arr), len(arr[0])
    
    for i in range(N):
        t = 0
        for j in range(1, M):
            if arr[i][j] == arr[i][j-1]:
                t += 1
            else:
                cnt += bool( t >= 5 ) * ( t - 2 )
                t = 0
        cnt += bool( t >= 5 ) * ( t - 2 )
        
    for j in range(M):
        t = 0
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                t += 1
            else:
                cnt += bool( t >= 5 ) * ( t - 2 )
                t = 0
        cnt += bool( t >= 5 ) * ( t - 2 )
        
    return cnt


def cond_B(arr):
    cnt = 0
    N, M = len(arr), len(arr[0])
    
    for i in range(N-1):
        for j in range(M-1):
            if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1]:
                cnt += 3
                
    return cnt

def cond_C(arr):
    cnt = 0
    N, M = len(arr), len(arr[0])
    tar = [[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1]]
    
    for i in range(N):
        for j in range(M-10):
            if arr[i][j:11] in tar:
                cnt += 40
    
    for i in range(N):
        for j in range(M):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
    for i in range(N):
        for j in range(M-10):
            if arr[i][j:11] in tar:
                cnt += 40
    
    for i in range(N):
        for j in range(M):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
                
    return cnt

def cond_D(arr):
    N, M = len(arr), len(arr[0])
    
    black = sum( sum( 1 for i in range(N) if arr[i][j] == 1 ) for j in range(M) )
    pct = black / (N*M) # black percentage
    
    return 10 * int(pct)

def evaluate(arr, used, condition):
    N, M = len(arr), len(arr[0])
    for i in range(N):
        for j in range(M):
            if  (i, j) not in used and condition(i, j):
                arr[i][j] = 1 - arr[i][j]
    
    return cond_A(arr) + cond_B(arr) + cond_C(arr) + cond_D(arr)
    
            
