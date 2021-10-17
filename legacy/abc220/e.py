
N, D = list(map(int, input().split()))
MOD = 998244353
dp = [0]*(2*(N-1)+1)

Minn = (D+3)//2
nowr = pow(2, (Minn-2), MOD)
nowl = pow(2, (Minn-2), MOD)

dp[Minn] = nowr*nowl

deep = Minn-1

for i in range(Minn + 1, N+1):
    deep += 1

    if deep == D:
        new = pow(2, deep-1, MOD)
    elif deep < D:
        new = (pow(2, deep-1, MOD)*pow(2, D-deep-1, MOD)) % MOD
    else:
        new = 0
    dp[i] = (dp[i-1]*3+new*2) % MOD

print((dp[N]*2) % MOD)
