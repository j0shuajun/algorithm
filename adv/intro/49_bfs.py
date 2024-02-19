import sys
sys.stdin = open('input.txt')

from collections import deque

n = int(input())
A = [input().strip() for _ in range(n)]

visit = [[0] * n for _ in range(n)]

cnt_list = []

def bfs(sr, sc):
    queue = deque([(sr, sc)])
    visit[sr][sc] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr, nc = r+dr, c+dc

            if nr<0 or nr>=n or nc<0 or nc>=n: continue
            if visit[nr][nc] == 1: continue
            if A[nr][nc] == '0': continue

            queue.append((nr, nc))
            visit[nr][nc] = 1
            cnt += 1

    return cnt

for r in range(n):
    for c in range(n):
        if A[r][c] == '1' and visit[r][c] == 0:
            cnt_list.append(bfs(r, c))

print(len(cnt_list), *sorted(cnt_list), sep='\n')