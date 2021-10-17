
N = int(input())
X, Y = map(int, input().split())

AB = [[int(i) for i in input().split()] for j in range(N)]
dp = [[[1000 for i in range(Y+1)] for n in range(X+1)] for j in range(N)]
a, b = AB[0]
a = min(X, a)
b = min(Y, b)
dp[0][a][b] = 1

for i in range(1, N):
    a, b = AB[i]
    a = min(X, a)
    b = min(Y, b)
    dp[i][a][b] = 1
    for j in range(X+1):
        for k in range(Y+1):
            if dp[i-1][j][k] != 1000:
                aj = min(X, j+a)
                bk = min(Y, k+b)
                dp[i][j][k] = min(dp[i-1][j][k], dp[i][j][k])
                dp[i][aj][bk] = min(dp[i-1][j][k]+1, dp[i][aj][bk])

if dp[N-1][X][Y] == 1000:
    print(-1)
else:
    print(dp[N-1][X][Y])
