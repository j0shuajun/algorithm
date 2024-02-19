import sys
sys.stdin = open('input.txt')

N, P = map(int, input().split())
num = []

def cycle(n):
    global N, P
    tmp = n*N % P
    if tmp==0:
        return print(1)
    elif tmp in num:
        return print(len(num))
    else:
        num.append(tmp)
    return cycle(tmp)

cycle(N)