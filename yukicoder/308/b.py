import sys
import heapq
sys.setrecursionlimit(10**6)  # 再帰関数使う時有効


def countup(now, R):
    # if len(root[now]) == 1 and root[now][0] in used:
    #     count[root[now][0]] += count[now]+1
    #     return
    # if now in used:
    #     return
    for next_ in root[now]:
        if next_ == R:
            continue
        countup(next_, now)
    if now == R:
        return
    global count
    count[R] += count[now]


N, Q = map(int, input().split())
root = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    root[a-1].append(b-1)
    root[b-1].append(a-1)
count = [1]*N
countup(0, 0)

ans = 0
for i in range(Q):
    p, x = map(int, input().split())

    ans += count[p-1]*x
    print(ans)
