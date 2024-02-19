import sys
sys.stdin = open('input.txt')

n = int(input())

def factorial(c):
    if c==1:
        print('1! = 1')
        return 1
    print(f'{c}! = {c} * {c-1}!')
    return c*factorial(c-1)

print(factorial(n))