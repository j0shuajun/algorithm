import sys
sys.stdin = open('input.txt')

A = [list(map(int, input().split())) for _ in range(5)]

calls = []
for _ in range(5):
    calls += list(map(int, input().split()))

def bingo():
    for i, call in enumerate(calls):
        cnt = 0
        for r in range(5):
            for c in range(5):
                if A[r][c] == call:
                    A[r][c] = 0

        for r in range(5):
            for c in range(5):
                for dr, dc in zip([0, 1, 1, 1], [1, 1, 0, -1]):
                    x, y = r, c
                    zero_cnt = 0
                    while 1:
                        if x==-1 or x==5 or y==-1 or y==5:
                            break
                        elif A[x][y]!=0:
                            break
                        else:
                            zero_cnt += 1
                            x, y = x+dr, y+dc
                    if zero_cnt==5:
                        cnt += 1
                        if cnt==3:
                            print(i+1)
                            return

bingo()