import sys
sys.stdin = open('input.txt')

N = int(input())
A = [0] + [int(input()) for _ in range(N)]
li = []


def pick(x):
    if x in visit:
        if x==a:
            li.append(x)
        return
    visit.add(x)
    pick(A[x])

for a in range(1, N+1):
    visit = set()
    pick(a)

print(len(li), *li, sep='\n')