import sys
sys.stdin = open('input.txt')

N, M, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

sr, sc, n, m = 0, 0, N, M

while 1:
    t = (n+m-2)*2

    for _ in range(T%t):
        r, c = sr, sc
        tmp = A[sr][sc]
        # 반시계 -> [우 하 좌 상] 순서로 탐색
        for dr, dc in zip([0,1,0,-1], [1,0,-1,0]):
            q = n-1 if dr else m-1
            for _ in range(q):
                A[r][c] = A[r+dr][c+dc]
                r, c = r+dr, c+dc
        A[sr+1][sc] = tmp

    sr, sc = sr+1, sc+1
    n, m = n-2, m-2
    if n==0 or m==0: break

for a in A:
    print(*a)


# import sys
# sys.stdin=open('input.txt')

# N, M, T = map(int,input().split())
# A = [list(map(int,input().split())) for _ in range(N)]

# sr, sc, n, m = 0, 0, N, M

# while 1:
#     t = (n+m-2)*2

#     for _ in range(T%t):
#         r, c = sr, sc
#         tmp = A[sr][sc]
#         for dr, dc in zip([0,1,0,-1],[1,0,-1,0]):
#             q = n-1 if dr else m-1
#             for _ in range(q):
#                 A[r][c] = A[r+dr][c+dc]
#                 r, c = r+dr, c+dc
#         A[sr+1][sc] = tmp

#     sr, sc = sr+1, sc+1
#     n, m = n-2, m-2
#     if n==0 or m==0: break

# for a in A:
#     print(*a)