# a=map(int, input().split())
import copy
MOD = 998244353
N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0 for i in range(3001)] for j in range(N+3)]

for i in range(a[0], b[0]+1):
    dp[0][i] = 1

for x in range(1, N):
    for y in range(a[x], b[x]+1):
        if y == a[x]:
            dp[x][y] = sum(dp[x-1][a[x-1]:y+1])
        else:
            dp[x][y] = dp[x][y-1]+dp[x-1][y]
        dp[x][y] %= MOD
print(sum(dp[N-1]) % MOD)
