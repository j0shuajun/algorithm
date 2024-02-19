import sys
sys.stdin = open('input.txt')

m, n, k = map(int, input().split())

A = [[1] * n for _ in range(m)]

for _ in range(k):
    sc, sr, ec, er = map(int, input().split())
    for r in range(sr, er):
        for c in range(sc, ec):
            A[r][c] = 0

def dfs(r, c):
    A[r][c] = 0
    cnt = 1

    for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        nr, nc = r+dr, c+dc
        
        if nr<0 or nr>=m or nc<0 or nc>=n: continue
        if A[nr][nc] == 0: continue

        cnt += dfs(nr, nc)

    return cnt

cnt_list = []

for r in range(m):
    for c in range(n):
        if A[r][c] == 1:
            cnt_list.append(dfs(r, c))

print(len(cnt_list))
print(*sorted(cnt_list))