N = int(input())
A = [[int(i) for i in input().split()] for j in range(N)]
MOD = int(1e9+7)
ans = 1
for i in range(N):
    ans *= sum(A[i])
    ans %= MOD
print(ans)
