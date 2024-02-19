import sys
sys.stdin = open('input.txt')

n = int(input())
# alpha = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I',
#          10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q',
#          18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

A = [[' ']*(2*n-1) for _ in range(2*n-1)]

r, c = 0, n-1
num = 0
rep = n-1

while 1:
    for dr, dc in zip([1, 1, -1, -1], [-1, 1, 1, -1]):
        for i in range(rep, 0, -1):
            A[r][c] = chr(num+65)
            # A[r][c] = alpha[num+1]
            num = (num+1)%26
            r, c = r+dr, c+dc
    r += 1
    rep -= 1

    if rep==0:
        A[r][c] = chr(num+65)
        # A[r][c] = alpha[num+1]
        break
    
for a in A:
    print(*a)