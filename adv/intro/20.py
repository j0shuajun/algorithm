import sys
import copy
sys.stdin = open('input.txt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

res = []


def flip():
    global A
    tmp_a = copy.deepcopy(A)
    A = [t[::-1] for t in tmp_a]

def rotate120():
    global A
    tmp_a = copy.deepcopy(A)
    for i in range(N):
        for j in range(i+1):
            A[i][j] = tmp_a[N-1-j][i-j]

def calc_diff():
    global A, B
    tmp = 0
    for a, b in zip(A, B):
        tmp += sum([(aa-bb)**2 for aa, bb in zip(a, b)])
        # tmp += sum(l != r for l, r in zip(a, b))
    res.append(tmp)


for _ in range(2):
    rotate120()
    calc_diff()
    rotate120()
    calc_diff()
    rotate120()
    calc_diff()
    flip()
    calc_diff()

print(min(res))


# import copy
# import sys
# sys.stdin=open('input.txt')

# N = int(input())
# A = [list(map(int,input().split())) for _ in range(N)]
# B = [list(map(int,input().split())) for _ in range(N)]
# C = [[0]*i for i in range(1,N+1)]
# res = N**2

# ## version1_1: 0, 120, 240 회전 각각 처리
# def pro1():
#     # A와 C의 차이를 확인, 최소값 업데이트
#     def update_min():
#         global res
#         diff = 0
#         for a, c in zip(A, C):
#             diff += sum(l != r for l, r in zip(a, c))
#         res = min(res, diff)

#     def rotate0():
#         global C
#         C = copy.deepcopy(B)

#     def rotate120():
#         # print(B)
#         for i in range(N):
#             for j in range(i + 1):
#                 # print(f'({i},{j}) ({N-1-j},{i-j})')
#                 C[i][j] = B[N - 1 - j][i - j]
#         # print(C)

#     def rotate240():
#         for i in range(N):
#             for j in range(i + 1):
#                 C[i][j] = B[N - 1 - (i - j)][N - 1 - i]

#     for i in range(2):
#         #0
#         rotate0()
#         update_min()
#         #120
#         rotate120()
#         update_min()
#         #240
#         rotate240()
#         update_min()

#         #reverse
#         for b in B:
#             b.reverse()

# ## version1_2: 120도 회전 3번 반복
# def pro2():
#     def update_min():
#         global res
#         diff = 0
#         for a, b in zip(A, B):
#             diff += sum(l != r for l, r in zip(a, b))
#         res = min(res, diff)

#     def rotate120():
#         C = copy.deepcopy(B)
#         for i in range(N):
#             for j in range(i + 1):
#                 B[i][j] = C[N - 1 - j][i - j]

#     for _ in range(2):
#         for _ in range(3):
#             rotate120()
#             update_min()
#         #reverse
#         for b in B:
#             b.reverse()

# ## version2, 120도로 여러번 회전
# def pro3():
#     def update_min():
#         global res
#         diff = 0
#         for a, b in zip(A, B):
#             diff += sum(l != r for l, r in zip(a, b))
#         res = min(res, diff)

#     def rotate120():
#         C = copy.deepcopy(B)
#         for i in range(N):
#             i2, j2 = N-1, i
#             for j in range(i + 1):
#                 B[i][j] = C[i2][j2]
#                 i2 -= 1
#                 j2 -= 1

#     for _ in range(2):
#         for _ in range(3):
#             rotate120()
#             update_min()
#         #reverse
#         for b in B:
#             b.reverse()

# # pro1()
# # pro2()
# pro3()
# print(res)