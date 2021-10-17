N = int(input())

M = [[0 for i in range(1001)] for j in range(1001)]
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    M[ly][lx] += 1
    M[ry][lx] -= 1
    M[ly][rx] -= 1
    M[ry][rx] += 1
    # M[ly][rx]+=1

pre_dp = [0]*1001
dp = [0]*1001
ans = [0]*(N+1)
now = 0
for x in range(1001):
    for y in range(1001):
        dp[y] = pre_dp[y]+M[y][x]
        now += dp[y]
        ans[now] += 1
    pre_dp = list(dp)
for i in range(N):

    print(ans[i+1])
