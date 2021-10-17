N, K = map(int, input().split())

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
n = 0
for i in range(N):
    n += abs(A[i]-B[i])
if K >= n and (K - n) % 2 == 0:
    print('Yes')
else:
    print('No')
