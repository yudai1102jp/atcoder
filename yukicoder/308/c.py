import sys
import heapq
sys.setrecursionlimit(10**6)  # 再帰関数使う時有効


H, W = map(int, input().split())
U, D, R, L, K, P = map(int, input().split())
x, y, xt, yt = map(int, input().split())
start = [x-1, y-1]
goal = [xt-1, yt-1]
goal_n = goal[0]*W+goal[1]
allow = [[1, 0], [0, 1], [-1, 0], [0, -1]]
allow_cost = [D, R, U, L]
C = [input() for i in range(H)]


# def fps(now, cost):

#     if now == goal:
#         return cost
#     ans = 10**13+8
#     for i in range(4):
#         nextx = now[0]+allow[i][0]
#         nexty = now[1]+allow[i][1]
#         if not (0 <= nextx < H and 0 <= nexty < W):
#             continue

#         if C[nextx][nexty] == '.':
#             new_cost = cost+allow_cost[i]
#         elif C[nextx][nexty] == '@':
#             new_cost = cost+allow_cost[i]+P
#         else:
#             continue
#         ans = min(ans, fps([nextx, nexty], new_cost))
#     return ans
dp = [[-1]*W for i in range(H)]
dp[start[0]][start[1]] = 0
q = []
heapq.heapify(q)
heapq.heappush(q, (0, start))
ok = set()
while q:
    cost, now = heapq.heappop(q)
    # now_n = [now_n//W, now_n % W]
    now_n = now*W+now
    if now_n == goal_n:
        break
    ok.add(now[0]*W+now[1])
    for i in range(4):
        nextx = now[0]+allow[i][0]
        nexty = now[1]+allow[i][1]
        if (not (0 <= nextx < H and 0 <= nexty < W)) or C[nextx][nexty] == '#' or nextx*W+nexty in ok:
            continue

        if C[nextx][nexty] == '.':
            new_cost = dp[now[0]][now[1]]+allow_cost[i]
        elif C[nextx][nexty] == '@':
            new_cost = dp[now[0]][now[1]]+allow_cost[i]+P

        if dp[nextx][nexty] == -1 or dp[nextx][nexty] > new_cost:
            dp[nextx][nexty] = new_cost
            heapq.heappush(q, (new_cost, [nextx, nexty]))

if dp[goal[0]][goal[1]] <= K and dp[goal[0]][goal[1]] != -1:
    print('Yes')
else:
    print('No')
