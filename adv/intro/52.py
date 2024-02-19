import sys
sys.stdin = open('input.txt')

from collections import deque

C, R = map(int, input().split())
A = [list(input().strip()) for _ in range(R)]

y, x = map(int, input().split())
x, y = x-1, y-1

visit = [[0]*C for _ in range(R)]

def bfs(sr, sc, dist):
    queue = deque([(sr, sc, dist)])
    visit[sr][sc] = dist

    while queue:
        r, c, d = queue.popleft()

        for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr, nc = r+dr, c+dc

            if nr<0 or nr>=R or nc<0 or nc>=C: continue
            if visit[nr][nc]: continue
            if A[nr][nc] == '0': continue

            queue.append((nr, nc, d+1))
            visit[nr][nc] = d+1

bfs(x, y, 3)

sec = 0
for v in visit:
    sec = max(sec, max(v))

cnt = 0
for r in range(R):
    for c in range(C):
        if int(A[r][c])==1 and visit[r][c]==0:
            cnt += 1

print(sec)
print(cnt)