import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
tile = [list(map(int, input().split())) for _ in range(n)]
res = 10000
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
exit_dir = [
    [1, -1, -1, 2],
    [3, 2, -1, -1],
    [-1, -1, 1, 0],
    [-1, 0, 3, -1],
    [0, -1, 2, -1],
    [-1, 1, -1, 3]
]

def get_dist():
    dist = 0
    r, c, d = 0, -1, 1
    while 1:
        r += dr[d]
        c += dc[d]
        if r==n-1 and c==n: return dist
        if r<0 or r>=n or c<0 or c>=n: return 10000
        d = exit_dir[tile[r][c]][d]
        if d==-1: return 10000
        dist += 1
    return dist

if k==0:
    res = get_dist()
else:
    for i in range(n):
        for j in range(n):
            old_num = tile[i][j]
            for new_num in range(6):
                if old_num == new_num: continue
                tile[i][j] = new_num
                res = min(res, get_dist())
            tile[i][j] = old_num

print(res if res<10000 else -1)