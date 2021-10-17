# a = list(input())
N = int(input())
A = list(map(int, input().split()))
# A=[[int(i) for i in input().split()] for j in range(N)]
now = 1
flag = True  # true gold
koudou = [0]*N
for i in range(1, N):
    if flag:
        if A[i-1] > A[i]:
            now *= A[i-1]
            flag = False
            koudou[i-1] = 1

    else:
        if A[i-1] < A[i]:
            now /= A[i-1]
            flag = True
            koudou[i-1] = 1

if not flag:
    koudou[-1] = 1
print(*koudou)
