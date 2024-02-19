import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0] * i for i in range(1, n+1)]

def make_A():
    r = c = -1 # 시작점 (-1, 1)
    m = n
    num = 0

    while 1:
        # 대각오른쪽아래 -> 왼쪽 -> 위로 -> ... 반복
        for dr, dc in zip([1, 0, -1], [1, -1, 0]):
            for _ in range(m):
                r, c = r+dr, c+dc # 이동하고 채울거니까 먼저 이동
                A[r][c] = num # 이동하고 채우기
                num = (num+1)%10 # 숫자는 0~9 계속 반복하니까 mod 사용
            m -= 1
            if m==0: return

make_A()
for a in A:
    print(*a)