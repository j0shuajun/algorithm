import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            A[i][j] = 1

res = 0

for i in range(1, 100):
    for j in range(1, 100):
        if A[i][j]:
            for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                if i+dx==100 or j+dy==100:
                    res += 1
                elif A[i+dx][j+dy] == 0:
                    res += 1

print(res)