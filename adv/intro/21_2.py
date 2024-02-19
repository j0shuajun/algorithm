import sys
sys.stdin = open('input.txt')

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

sx, sy = 0, 0
n, m = N, M

while 1:
    r = (n+m-2)*2

    for _ in range(R%r):
        x, y = sx, sy
        tmp = A[sx][sy]
        # 시계 -> [하 우 상 좌] 순서로 탐색
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            rep = n-1 if dx else m-1
            for _ in range(rep):
                A[x][y] = A[x+dx][y+dy]
                x, y = x+dx, y+dy
        A[sx][sy+1] = tmp

    sx, sy = sx+1, sy+1
    n, m = n-2, m-2

    if n==0 or m==0:
        break

for a in A:
    print(*a)