import sys

sys.stdin = open("input.txt")

N = int(input())
works = [tuple(map(int, input().split())) for _ in range(N)]

total = 0


def work(t, p):
    global total

    if t > N:
        return
    if t == N:
        total = max(total, p)
        return

    work(t + 1, p)
    work(t + works[t][0], p + works[t][1])


work(0, 0)
print(total)
