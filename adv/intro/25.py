import sys
sys.stdin = open('input.txt')

A = [list(map(int, input().split())) for _ in range(19)]

def gomoku():
    for i in range(19):
        for j in range(19):
            if A[i][j] != 0:
                tmp = A[i][j]
                for dr, dc in zip([-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]):
                    cnt = 1
                    x, y = i, j
                    while 1:
                        x, y = x+dr, y+dc
                        if x==-1 or x==19 or y==-1 or y==19:
                            break
                        if A[x][y]==tmp:
                            cnt += 1
                        else:
                            break
                    if cnt == 5 and A[i-dr][j-dc]!=tmp:
                        print(tmp)
                        if dc >= 0:
                            print(i+1, j+1)
                        else:
                            print(x-dr+1, y-dc+1)
                        return
    print(0)

gomoku()