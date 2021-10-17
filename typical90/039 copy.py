import sys  # 追加
YES = 'Yes'
NO = 'No'
TAKAHASHI = 'Takahashi'
AOKI = 'Aoki'
sys.setrecursionlimit(500*500)

N = int(input())
ab = [[int(i) for i in input().split()] for j in range(N-1)]

load = [[] for i in range(N)]

for i in range(N-1):
    a, b = ab[i]
    load[a-1].append(b-1)
    load[b-1].append(a-1)

dp = [0]*N


def dfs(top, pre):
    count = 1
    for next in load[top]:
        if next == pre:
            continue
        count += dfs(next, top)
    global dp
    dp[top] = count
    return count


dfs(0, -1)

ans = 0
for d in dp:
    ans += d*(N-d)
print(ans)
