N, L = map(int, input().split())

MOD = int(1e9+7)

dp = [0]*(N+3)
dp[0] = 1

for i in range(N):
    dp[i] %= MOD
    dp[i+1] += dp[i]
    if i+L < N+2:
        dp[i+L] += dp[i]
print(dp[N] % MOD)
