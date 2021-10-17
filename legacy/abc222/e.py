# a=map(int, input().split())
import copy
import sys
sys.setrecursionlimit(500*500)

MOD = 998244353

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
load = [[] for i in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    load[u-1].append((v-1, i))
    load[v-1].append((u-1, i))

pass_c = [0]*(N-1)


def dfs(pre, now, goal):
    global pass_c
    if now == goal:
        return True
    for ne, num in load[now]:
        if ne == pre:
            continue
        if dfs(now, ne, goal):
            pass_c[num] += 1
            return True
    return False


for i in range(M-1):
    now = A[i]
    ne = A[i+1]
    dfs(-1, now-1, ne-1)


Sum = sum(pass_c)
if Sum % 2 != K % 2:
    print(0)
    exit()
if (K+Sum)//2 >= 0 and (-K+Sum)//2 >= 0:
    Wa = min((K+Sum)//2, (-K+Sum)//2)
else:
    Wa = max((K+Sum)//2, (-K+Sum)//2)


dp = [[0 for i in range(Wa+1)] for j in range(len(pass_c)+3)]
dp[0][0] = 1

for i in range(len(pass_c)):
    for j in range(Wa+1):
        dp[i+1][j] += dp[i][j]
        if j >= pass_c[i]:
            dp[i+1][j] += dp[i][j-pass_c[i]]
        dp[i+1][j] %= MOD

print(dp[len(pass_c)][Wa])
