import sys
sys.stdin = open('input.txt')

from collections import deque

M, N = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]

# def bfs(sr, sc):
#     visit = [[0] * M for _ in range(N)]

#     queue = deque([(sr, sc, 1)])
#     visit[sr][sc] = 1

#     while queue:
#         r, c, d = queue.popleft()

#         for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
#             nr, nc = r+dr, c+dc

#             if nr<0 or nr>=N or nc<0 or nc>=M: continue
#             if visit[nr][nc]: continue
#             if A[nr][nc] == 1 or A[nr][nc] == -1: continue

#             queue.append((nr, nc, d+1))
#             visit[nr][nc] = 1
#             if A[nr][nc]:
#                 A[nr][nc] = min(A[nr][nc], d+1)
#             else:
#                 A[nr][nc] = d+1

# for r in range(N):
#     for c in range(M):
#         if A[r][c]==1:
#             bfs(r, c)

# zero = 0
# for a in A:
#     if 0 in a:
#         zero = 1

# if zero:
#     print(-1)
# else:
#     MM = 0
#     for a in A:
#         MM = max(MM, max(a))
#     print(MM-1)

que = deque()
for i in range(N):
    for j in range(M):
        if A[i][j] == 1:
            que.append((i,j,0))
            A[i][j] = -1

def bfs():
    while que:
        r,c,day = que.popleft()
        for dr, dc in zip([-1,0,1,0],[0,1,0,-1]):
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M: continue
            if A[nr][nc] == -1: continue

            que.append((nr,nc,day+1))
            A[nr][nc] = -1

    for a in A:
        if not all(a): return -1
        # if a.count(0): return -1
    return day

print(bfs())