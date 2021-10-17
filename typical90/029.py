W, N = map(int, input().split())
dp = [[0, 0], [W+1, 0]]

max_height = [0, W+1, 0]
for i in range(N):
    l, r = map(int, input().split())
    dp_len = len(dp)
    lclose_kaburi = False
    rclose_kaburi = False
    lclose = 0
    ng = dp_len
    while ng-lclose > 1:
        now = (lclose+ng)//2

        if dp[now][0] < l:
            lclose = now
        elif dp[now][0] == l:
            lclose = now
            lclose_kaburi = True
            break
        else:
            ng = now

    rclose = lclose
    ng = dp_len
    while ng - rclose > 1:
        now = (rclose+ng)//2
        if dp[now][0] <= r:
            rclose = now
        else:
            if dp[now][0] == r+1:
                rclose_kaburi = True
            ng = now

    height = 0
    if max_height[1] < l or r < max_height[0]:
        for h in range(lclose, rclose+1):
            height = max(height, dp[h][1])
    else:
        height = max_height[2]

    if lclose_kaburi:
        new_dp = dp[:lclose]
    else:
        new_dp = dp[:lclose+1]
    new_dp.append([l, height+1])

    if rclose_kaburi:
        new_dp = new_dp+dp[rclose+1:]
    else:
        new_dp.append([r+1, dp[rclose][1]])
        new_dp = new_dp+dp[rclose+1:]

    dp = new_dp
    print(height+1)
    if max_height[2] < height+1:
        max_height = [l, r, height+1]

    # high = max(dp[l:r+1])+1
    # print(high)
    # for j in range(l, r+1):
    #     dp[j] = high
