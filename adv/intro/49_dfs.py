import sys
sys.stdin = open('input.txt')

n = int(input())
A = [input().strip() for _ in range(n)]

visit = [[0] * n for _ in range(n)]
cnt_list = []

def dfs(r, c):
    global cnt
    cnt += 1
    visit[r][c] = 1

    for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        nr, nc = r+dr, c+dc

        if nr<0 or nr>=n or nc<0 or nc>=n: continue
        if visit[nr][nc] == 1: continue
        if A[nr][nc] == '0': continue

        dfs(nr, nc)

for r in range(n):
    for c in range(n):
        if A[r][c] == '1' and visit[r][c] == 0:
            cnt = 0
            dfs(r, c)
            cnt_list.append(cnt)

print(len(cnt_list), *sorted(cnt_list), sep='\n')