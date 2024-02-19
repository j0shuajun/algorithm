import sys
sys.stdin=open('input.txt')

n = int(input())
A = [[1]*n for _ in range(n)]   # (0,0)을 1로 채워놓고 시작

def fill_A():
    r = c = 0
    num = 1
    while 1:
        # 한칸 이동
        # 1)아래 2)오른쪽
        if r < n-1: r += 1
        else: c += 1
        
        # 삽입 후 이동
        # 우상 방향
        while 1:
            num += 1
            A[r][c] = num
            if num==n*n: return
            if r == 0 or c == n-1: break
            r -= 1
            c += 1
    
        # 한칸 이동
        # 1)오른쪽 2)아래
        if c < n-1: c += 1
        else: r += 1
    
        # 삽입 후 이동
        # 좌하 방향
        while 1:
            num += 1
            A[r][c] = num
            if num==n*n: return
            if r == n-1 or c == 0: break
            r += 1
            c -= 1

fill_A()

for a in A:
    print(*a)