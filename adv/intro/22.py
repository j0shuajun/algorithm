import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            A[i][j] = 1

print(sum(sum(a) for a in A))