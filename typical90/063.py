H, W = map(int, input().split())

P = [[int(i) for i in input().split()] for j in range(H)]

dp = [[0 for i in range(H*W+1)] for j in range(2**8)]


for i in range(1, 2**H):
    S = [s for s in range(8) if i & 1 << s]
    for w in range(W):
        flag = True
        now = 0
        for h in S:
            if now == 0:
                now = P[h][w]
            elif P[h][w] != now:
                flag = False
                break
        if flag:
            dp[i][now] += len(S)

print(max([max(i) for i in dp]))
