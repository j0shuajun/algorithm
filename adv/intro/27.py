import sys
sys.stdin = open('input.txt')

from itertools import permutations

res = 0
info = []

for _ in range(int(input())):
    i, s, b = input().split()
    info.append((i, int(s), int(b)))

def check(num):
    for q, s, b in info:
        st = ba = 0
        for i in range(3):
            for j in range(3):
                if q[i]==num[j] and i==j:
                    st += 1
                if q[i]==num[j] and i!=j:
                    ba += 1
        if st!=s:
            return False
        if ba!=b:
            return False
    return True

for a, b, c in permutations(range(1, 10), 3):
    num = str(100*a + 10*b + c)
    if check(num):
        res += 1
        
print(res)