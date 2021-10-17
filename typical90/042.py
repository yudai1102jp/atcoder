import sys  # 追加
YES = 'Yes'
NO = 'No'
TAKAHASHI = 'Takahashi'
AOKI = 'Aoki'
sys.setrecursionlimit(500*500)
MOD = int(1e9+7)
K = int(input())


if K % 9:
    print(0)
else:
    dp = [0]*(K+1)
    dp[0] = 1
    for i in range(1, 1+K):
        for j in range(1, 1+min(i, 9)):
            dp[i] += dp[i-j]
            dp[i] %= MOD
    print(dp[K])
