import sys
input  = sys.stdin.readline

def possiblerotation(n, arr, s):
    val = arr[s]
    dest = 0
    q = 0
    flag = False
    if arr[s] == 0:
        flag = True 
    else:
        for i in range(n):
            if arr[i] == 0:
                dest = arr[i]
                q = i
        if q < s:
            while arr[s] != 0 and n > 0:
                s -= arr[s]
                if arr[s] == 0:
                    flag = True
                n -= 1 
        if q > s:
            while arr[s] != 0 and n > 0:
                s += arr[s]
                if arr[s] == 0:
                    flag = True
                n -= 1    
            
        if flag:
            return 1
        else:
            return 0

def printpossiblerotation(n, arr, s):
    if possiblerotation(n, arr, s) == 1:
        print('YES')
    else:
        print('NO')
    
    
    
t = int(input())
for i in range(t):
    len = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    printpossiblerotation(len, arr, s)

