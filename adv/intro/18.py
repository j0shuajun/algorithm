import sys
sys.stdin = open('input.txt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def rotate90():
    tmp = [a[:] for a in A]

    for i in range(N):
        for j in range(N):
            A[j][N-1-i] = tmp[i][j]


def rotate():
    global d
    if d == 90:
        A = rotate90()
    if d == 180:
        for _ in range(2):
            A = rotate90()
    if d == 270:
        for _ in range(3):
            A = rotate90()


while 1:
    d = int(input())
    if d == 0:
        break
    rotate()
    for a in A:
        print(*a)



# import copy
# import sys
# sys.stdin=open('input.txt')

# N = int(input())
# # A = [list(map(int,input().split())) for _ in range(N)]

# A = []
# for i in range(N):
#     li = list(map(int,input().split()))
#     A.append(li)

# def rotate():
#     tmp = copy.deepcopy(A)
#     for i in range(N):
#         for j in range(N):
#             if d == 90: A[j][N-1-i] = tmp[i][j]
#             if d == 180: A[N-1-i][N-1-j] = tmp[i][j]
#             if d == 270: A[N-1-j][i] = tmp[i][j]

# while 1:
#     d = int(input())
#     if d == 0: break
#     rotate()
#     for a in A:
#         print(*a)


# def practice():
#     # reference copy
#     A = [[0,0,0] for _ in range(3)]
#     B = A

#     B[0][0] = 10
#     B[1] = [20,0,0]
#     print(A)

#     # shallow copy
#     A = [[0,0,0] for _ in range(3)]
#     ## 1
#     B = A[:]

#     ## 2
#     B = A.copy()

#     B[0][0] = 10
#     B[1] = [20,0,0]
#     print(A)

#     # deep copy
#     A = [[0,0,0] for _ in range(3)]

#     ## 1
#     B = []
#     for a in A:
#         B.append(a[:])

#     ## 2
#     B = [a[:] for a in A]

#     ## 3
#     B = copy.deepcopy(A)

#     B[0][0] = 10
#     B[1] = [20,0,0]
#     print(A)

# # practice()