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


def cal(top, pre, ans,  dist, count):
    incre_dist = 0
    incre_count = 0
    for next in load[top]:
        if next == pre:
            continue
        incre_dist2, incre_count2, ans, count = cal(
            next, top, ans+dist+count, dist+count, count+1)
        dist += incre_dist2+incre_count2
        incre_dist += incre_count2+incre_dist2
        incre_count += incre_count2
    return incre_dist, incre_count+1, ans, count


for i in range(N):
    if len(load[i]) == 1:
        start = i
        break

print(cal(start, -1, 0, 0, 1)[2])
