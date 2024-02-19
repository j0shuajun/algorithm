import sys
sys.stdin = open('input.txt')

from collections import deque

R, C = map(int, input().split())
kr, kc, pr, pc = map(int, input().split())
kr, kc, pr, pc = kr-1, kc-1, pr-1, pc-1

A = [[0] * C for _ in range(R)]

def bfs(sr, sc):
    queue = deque([(sr, sc, 0)])
    A[sr][sc] = 1

    while queue:
        r, c, d = queue.popleft()
        if r==pr and c==pc:
            return print(d)

        for dr, dc in zip([-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]):
            nr, nc = r+dr, c+dc
            
            if nr<0 or nr>=R or nc<0 or nc>=C: continue
            if A[nr][nc]: continue

            queue.append((nr, nc, d+1))
            A[nr][nc] = 1

bfs(kr, kc)