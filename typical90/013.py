import heapq
from heapq import heappush, heappop


N, M = map(int, input().split())

Node = [[] for i in range(N+1)]
INF = int(1e10)
for i in range(M):
    a, b, c = map(int, input().split())
    Node[a].append([b, c])
    Node[b].append([a, c])

cost = [-1]*(N+1)

cost[1] = 0

q = [1]
while q:
    now = heappop(q)

    for next in Node[now]:
        Co = cost[now]+next[1]
        if cost[next[0]] == -1 or Co < cost[next[0]]:
            cost[next[0]] = Co
            if next[0] not in q:

                heappush(q, next[0])


recost = [-1]*(N+1)
ok = [0]*(N+1)

ok[N] = 1
recost[N] = 0

heappush(q, N)
while q:
    now = heappop(q)
    ok[now] = 1
    for next in Node[now]:
        Co = recost[now]+next[1]
        if recost[next[0]] == -1 or Co < recost[next[0]]:
            recost[next[0]] = Co
            # if not ok[next[0]] and next[0] not in q:
            if next[0] not in q:

                heappush(q, next[0])


for i in range(1, 1+N):

    print(recost[i]+cost[i])
