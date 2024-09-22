import sys

sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    cnt = 0
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))

    for i in range(N):
        if A[i] > max(B):
            cnt += M
            continue
        if A[i] <= min(B):
            continue
        for j in range(M):
            if A[i] <= B[j]:
                cnt += j
                break
    print(cnt)


## Time Limit Exceed
## A도 정렬해서 다시 해보자