import sys
sys.stdin = open('input.txt')

d, k = map(int, input().split())

cnt_a = cnt_b = 1

if d > 3:
    for _ in range(3, d):
        tmp = cnt_a + cnt_b
        cnt_a = cnt_b
        cnt_b = tmp

def tiger():
    for a in range(1, k):
        for b in range(a, k):
            if cnt_a*a + cnt_b*b == k:
                print(a, b, sep='\n')
                return
            
tiger()