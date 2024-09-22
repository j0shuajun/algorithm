import sys

sys.stdin = open("input.txt")

N = int(input())
l = list(map(int, input().split()))

h = 0  # head
t = N - 1  # tail

m = 1e10

while h < t:
    s = l[h] + l[t]

    if abs(s) < m:
        h_out = h
        t_out = t
        m = abs(s)
    
    if abs(l[h]) < abs(l[t]):
        t -= 1
    else:
        h += 1

print(l[h_out], l[t_out])