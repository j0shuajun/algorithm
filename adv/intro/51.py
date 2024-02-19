import sys
sys.stdin = open('input.txt')

from collections import deque

m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    air[sr][sc] = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr, nc = r+dr, c+dc
            
            if nr<0 or nr>=m or nc<0 or nc>=n: continue
            if air[nr][nc]: continue
            if A[nr][nc]: continue

            queue.append((nr, nc))
            air[nr][nc] = 1

def melt():
    melted = []
    for r in range(m):
        for c in range(n):
            if A[r][c] == 0: continue
            for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and air[nr][nc]:
                    melted.append((r, c))
                    A[r][c] = 0
                    break
    return melted

hr = 0
last = 0

air = [[0]*n for _ in range(m)]
sr, sc = 0, 0

while 1:
    remain = 0
    for a in A:
        remain += sum(a)

    if remain:
        last = remain
    else:
        break

    hr += 1
    
    if hr>1:
        for sr, sc in melted:
            bfs(sr, sc)   
        melted = melt()
    else:
        bfs(sr, sc)
        melted = melt()
    
print(hr)
print(last)