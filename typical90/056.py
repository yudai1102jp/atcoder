from collections import deque
from typing import Collection


N, S = map(int, input().split())
AB = [[int(i) for i in input().split()] for j in range(N)]
dp = [[-1 for i in range(S+4)] for j in range(N+1)]

if AB[0][0] <= S:
    dp[0][AB[0][0]] = 0
if AB[0][1] <= S:
    dp[0][AB[0][1]] = 1

for i in range(1, N):
    for j in range(S):
        if dp[i-1][j] != -1:
            if j+AB[i][0] <= S:
                dp[i][j+AB[i][0]] = 0
            if j+AB[i][1] <= S:
                dp[i][j+AB[i][1]] = 1

if dp[N-1][S] == -1:
    print('Impossible')
else:
    ans = deque()
    now = S
    for i in range(N-1, -1, -1):
        ans.append(dp[i][now])
        now -= AB[i][dp[i][now]]
    for i in range(N):
        print('A' if ans.pop() == 0 else 'B', end='')
