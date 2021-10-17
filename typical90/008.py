import math
MOD = int(1e9+7)
N = int(input())
S = input()
at = list('atcoder')
atcoder = [[] for i in range(len(at))]

now_atcoder = 0
for i in range(len(S)):
    if S[i] in at:
        atcoder[at.index(S[i])].append(i)


for i in atcoder:
    if not i:
        print(0)
        exit()


ans = 0

dp = [[[i, 0] for i in at] for at in atcoder]
for a in range(len(dp[0])):
    dp[0][a][1] = 1

for i in range(6):
    Sum = 0
    k = 0
    for j in range(len(dp[i+1])):
        while k < len(dp[i]):
            if dp[i+1][j][0] > dp[i][k][0]:
                Sum = (Sum + dp[i][k][1]) % MOD
                k += 1
            else:
                break
        dp[i+1][j][1] = Sum

ans = 0
for i in dp[-1]:
    ans += i[1]
print(ans % MOD)
