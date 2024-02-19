import sys
sys.stdin = open('input.txt')

T, N, K = map(int, input().split())

A = [0]*N

def recur1(c):
    if c==N:
        print(*A)
        return

    for i in range(1, K+1):
        if c==0:
            A[c] = i
        elif i >= A[c-1]:
            A[c] = i
        else:
            continue
        recur1(c+1)

def recur2(c):
    if c==N:
        print(*A)
        return

    for i in range(1, K+1):
        if c==0:
            A[c] = i
        elif i > A[c-1]:
            A[c] = i
        else:
            continue
        recur2(c+1)

if T==1:
    recur1(0)
else:
    recur2(0)