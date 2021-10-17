h, w = map(int, input().split())

mod = 10**9+7
dp = [list([0 for i in range(w+1)]) for j in range(h+1)]
X = [list([0 for i in range(w+1)]) for j in range(h+1)]
Y = [list([0 for i in range(w+1)]) for j in range(h+1)]
Z = [list([0 for i in range(w+1)]) for j in range(h+1)]
s = [input() for i in range(h)]

dp[0][0] = 0
for i in range(1, h):
    if s[i][0]=='.':
        dp[i][0] += dp[i-1][0]+1
        Y[i][0] = dp[i][0]
    else:
        break
for i in range(1, w):
    if s[0][i]=='.':
        dp[0][i] += dp[0][i-1]+1
        X[0][i] = dp[0][i]
    else:
        break

for y in range(1, h):
    for x in range(1, w):
        if s[y][x] == '.':
            X[y][x] = X[y][x-1] + dp[y][x-1]
            Y[y][x] = Y[y-1][x] + dp[y-1][x]
            Z[y][x] = Z[y-1][x-1] + dp[y-1][x-1]
            dp[y][x] = X[y][x]+Y[y][x]+Z[y][x]


print(dp[h-1][w-1])
