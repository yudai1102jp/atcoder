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

ans = [0]*N


def cal(top, pre):
    count = 1
    dist = 0
    for next in load[top]:
        if next == pre:
            continue
        ans, count2 = cal(next, top)
        dist += ans
        count += count2
    return dist+count, count


for i in range(N):
    if len(load[i]) == 1:
        start = i
        break

dist = cal(start, -1)[0]-N
ans[start] = dist

part = [0]*Nœœ


def write(top, pre):
    count = 1
    for next in load[top]:
        if next == pre:
            continue
        count += write(next, top)
    part[top] = count
    return count


write(start, -1)


def dfs(top, pre, dist):
    ans[top] = dist

    for next in load[top]:
        if next == pre:
            continue
        dfs(next, top, dist+(N-part[next])-part[next])


dfs(start, -1, dist)
for i in range(N):
    print(ans[i])
