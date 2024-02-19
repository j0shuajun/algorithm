import sys
sys.stdin = open('input.txt')

from collections import deque

queue = deque()

for _ in range(int(input())):
    cmd, *val = input().split()

    if cmd == 'i':
        queue.append(int(val[0]))
    if cmd == 'c':
        print(len(queue))
    if cmd == 'o':
        if queue:
            print(queue.popleft())
        else:
            print('empty')
        
    