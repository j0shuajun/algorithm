import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0]*n for _ in range(n)]

r, c = 0, n//2
num = 1

A[r][c] = num

while 1:
    if num%n==0:
        r += 1
    elif r==0:
        r = n-1
        c -= 1
    elif c==0:
        r -= 1
        c = n-1
    else:
        r -= 1
        c -= 1
    
    num += 1
    
    A[r][c] = num
    if num==n**2:
        break

for a in A:
    print(*a)