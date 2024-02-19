import sys
sys.stdin = open('input.txt')

n = int(input())

if 1 <= n < 100 and n%2:
    n = n//2 + 1
    for i in range(n):
        print(' '*i + '*'*(2*i+1))
    for i in range(n-2, -1, -1):
        print(' '*i + '*'*(2*i+1))
else:
    print('INPUT ERROR!')