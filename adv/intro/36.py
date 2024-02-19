import sys
sys.stdin = open('input.txt')

n = int(input())
A = [0] * (n+1)

def fibonacci(num):
    if num==1 or num==2:
        return 1
    if A[num]:
        return A[num]
    A[num] = fibonacci(num-1) + fibonacci(num-2)
    return A[num]

print(fibonacci(n))