import sys
import math
from heapq import heappop, heappush
sys.setrecursionlimit(2500000)
n, m, x, y = map(int, input().split())
abtk = []

dic = {i: [] for i in range(1, n+1)}
abtk = [None]*m
for i in range(m):
    abtk[i] = list(map(int, input().split()))
    a, b, t, k = abtk[i]

    dic[a].append(i)
    dic[b].append(i)


inf = pow(10, 15)
time = {i: inf for i in range(1, n+1)}
time[x] = 0


start_node = x
routes_from_start = {n: math.inf for n in range(1, n+1)}

# 最初の頂点にゼロを設定
routes_from_start[start_node] = 0

que=

minHeap = []

# 最初の頂点を追加
heappush(minHeap, (0, start_node))

# ヒープがなくなるまで探索
while minHeap:
    (cost, current_node) = heappop(minHeap)

    # priority keyは重複するのでここでチェックする
    if cost > routes_from_start[current_node]:
        continue

    for node in current_node.routes:
        price_info = current_node.routes[node]
        if routes_from_start[node] > price_info + routes_from_start[current_node]:
            routes_from_start[node] = price_info + routes_from_start[current_node]
            # 更新されたらpriorityに値を追加
            heappush(minHeap, (price_info + routes_from_start[current_node], node))

return routes_from_start[nodes[-1]]


dp(x, 0)

if time[y] == inf:
    print(-1)
else:
    print(time[y])
