import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0] * n for _ in range(n)]

sx, sy = 0, 0

num = 1
rep = n-1

while 1:
    x, y = sx, sy
    if n%2==0 and num==n**2+1:
        break

    A[x][y] = num

    if n%2==1 and num==n**2:
        break

    # 시계 -> 우 하 좌 상
    for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
        for _ in range(rep):
            x, y = x+dx, y+dy
            if (x==sx and y==sy):
                num += 1
                break
            num += 1
            A[x][y] = num
        
    sx, sy = sx+1, sy+1
    rep -= 2

for a in A:
    print(*a)