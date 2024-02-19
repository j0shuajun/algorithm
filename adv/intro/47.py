import sys
sys.stdin = open('input.txt')

stack = []

for _ in range(int(input())):
    cmd, *val = input().split()

    if cmd == 'i':
        stack.append(int(val[0]))
    if cmd == 'o':
        if stack:
            print(stack.pop())
        else:
            print('empty')
    if cmd == 'c':
        print(len(stack))