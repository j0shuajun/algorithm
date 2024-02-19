import sys
sys.stdin = open('input.txt')

from collections import deque

m, n, k = map(int, input().split())

A = [[0] * n for _ in range(m)]
visit = [[0] * n for _ in range(m)]

for _ in range(k):
    sc, sr, ec, er = map(int, input().split())
    for r in range(sr, er):
        for c in range(sc, ec):
            A[r][c] = 1

def bfs(sr, sc):
    queue = deque([(sr, sc)])
    visit[sr][sc] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr, nc = r+dr, c+dc

            if nr<0 or nr>=m or nc<0 or nc>=n: continue
            if visit[nr][nc] == 1: continue
            if A[nr][nc] == 1: continue

            cnt += 1
            queue.append((nr, nc))
            visit[nr][nc] = 1

    return cnt

cnt_list = []

for r in range(m):
    for c in range(n):
        if A[r][c] == 0 and visit[r][c] == 0:
            cnt_list.append(bfs(r, c))

print(len(cnt_list))
print(*sorted(cnt_list))