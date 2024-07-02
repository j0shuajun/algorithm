import sys

sys.stdin = open("input.txt")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

cnt = 0


def check(r, c, d):
    turn = False
    for dr, dc in zip(dR, dC):
        if A[r + dr][c + dc] == 0:
            turn = True
            d = (d - 1) % 4
            while A[r + dR[d]][c + dC[d]] != 0:
                d = (d - 1) % 4
            r += dR[d]
            c += dC[d]
            return r, c, d, turn
    return r, c, d, turn


def main(r, c, d):
    global cnt, A

    if A[r][c] == 0:
        A[r][c] = 2
        cnt += 1

    r, c, d, turn = check(r, c, d)

    if not turn:
        if A[r + dR[(d - 2) % 4]][c + dC[(d - 2) % 4]] != 1:
            r += dR[(d - 2) % 4]
            c += dC[(d - 2) % 4]

    return r, c, d


while 1:
    nr, nc, nd = main(r, c, d)
    if nr==r and nc==c:
        break
    else:
        r, c, d = nr, nc, nd

print(cnt)