# a = list(input())
import heapq
# N = int(input())
N, M = list(map(int, input().split()))
AB = [[int(i) for i in input().split()] for j in range(M)]


allow = [[] for i in range(N+1)]
permit = [set() for i in range(N+1)]
not_ok = set()
ok_list = [True for i in range(N+1)]
for i in range(M):
    allow[AB[i][0]].append(AB[i][1])
    permit[AB[i][1]].add(AB[i][0])
    ok_list[AB[i][1]] = False
now = []
for i in range(1, N+1):
    if ok_list[i]:
        now.append(i)
heapq.heapify(now)

ans = []
ans_id = 0

used = set()
ok_used = set(now)
for i in range(N):
    if not now:
        break

    Min = heapq.heappop(now)
    ans.append(Min)
    used.add(Min)
    next = allow[Min]
    for ne in next:

        if (ne not in ok_used) and (permit[ne] <= used):
            heapq.heappush(now, ne)
            ok_used.add(ne)
if len(ans) == N:
    print(*ans)
else:
    print(-1)
