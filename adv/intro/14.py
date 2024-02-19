import sys
import copy
sys.stdin = open('input.txt')

n, typ = map(int, input().split())
A = [[0]*i for i in range(1, n+1)]

def pascal():
    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]


def type_check():
    global A
    if typ==2:
        A = [['']*i + a[:] for i, a in enumerate(A[::-1])]
    if typ==3:
        tmp = copy.deepcopy(A)
        for i in range(n):
            for j in range(i+1):
                A[i][j] = tmp[n-1-j][n-1-i]


pascal()
type_check()

for a in A:
    print(*a)