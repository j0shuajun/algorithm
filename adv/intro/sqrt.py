import sys
sys.stdin = open('input.txt')

n = int(input())

low, high = 1, n

while low <= high:
    mid = (low + high) // 2
    if mid**2 == n:
        print(mid)
        break
    elif mid**2 < n:
        low = mid + 1
    else:
        high = mid - 1

if low > high:
    print(high)
