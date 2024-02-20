import sys
sys.stdin = open('input.txt')

from collections import deque, defaultdict

N, M, C = map(int, input().split()) # C: battery
A = [list(map(int, input().split())) for _ in range(N)]     # 0: space, 1: wall

tr, tc = map(int, input().split())  # taxi
tr, tc = tr-1, tc-1

passenger = [list(map(int, input().split())) for _ in range(M)]     # sr, sc, er, ec
for i, p in enumerate(passenger):
    passenger[i] = [v-1 for v in p]

p_dict = defaultdict(int)
for p in passenger:
    p_dict[(p[0], p[1])]

a_dict = {}
for p in passenger:
    a_dict[(p[0], p[1])] = ([p[2], p[3]])


def p_bfs(sr, sc):
    global p_cnt
    que = deque([(sr, sc, 0)])
    visit[sr][sc] = 1

    while que:
        x, y, c = que.popleft()
        for k, v in p_dict:
            if x==k and y==v:
                p_dict[(k, v)] = c
                p_cnt += 1

        for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr, nc = x+dr, y+dc

            if nr<0 or nr>=N or nc<0 or nc>=N: continue
            if visit[nr][nc]: continue
            if A[nr][nc]: continue
            
            que.append((nr, nc, c+1))
            visit[nr][nc] = 1


def a_bfs(sr, sc):
    global a_cnt
    que = deque([(sr, sc, 0)])
    visit[sr][sc] = 0

    while que:
        x, y, c = que.popleft()

        for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr, nc = x+dr, y+dc

            if nr<0 or nr>=N or nc<0 or nc>=N: continue
            if visit[nr][nc]: continue
            if A[nr][nc]: continue

            if nr==er and nc==ec:
                a_cnt = 1
                return c+1
            
            que.append((nr, nc, c+1))
            visit[nr][nc] = 1


for _ in range(len(passenger)):
    visit = [[0] * N for _ in range(N)]
    p_cnt = 0
    p_bfs(tr, tc)

    if p_cnt < len(p_dict):
        print(-1)
        break

    p_dict = sorted(p_dict.items(), key = lambda x: (x[1], x[0][0], x[0][1]))
    start, dist = p_dict[0][0], p_dict[0][1]

    if C<dist:
        print(-1)
        break
    else:
        tr, tc = start
        C -= dist
    
    er, ec = a_dict[(tr, tc)]

    visit = [[0] * N for _ in range(N)]
    a_cnt = 0
    move_dist = a_bfs(tr, tc)

    if a_cnt==0:
        print(-1)
        break

    if C<move_dist:
        print(-1)
        break
    else:
        tr, tc = er, ec
        C -= move_dist
        C += 2*move_dist

    p_dict = dict(p_dict[1:])

if not p_dict:
    print(C)