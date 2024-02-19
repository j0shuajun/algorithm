import sys
sys.stdin = open('input.txt')

from collections import defaultdict

n = int(input())
info = [[] for _ in range(n+1)]
part = defaultdict(int)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    info[a].append((b, c))

def recur(cur, cnt):
    if not info[cur]:
        part[cur] += cnt
        return
    
    for next, c in info[cur]:
        recur(next, cnt*c)

recur(n, 1)

for i in range(1, n):
    if not info[i]:
        print(i, part[i])