import sys
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


def dp(x):
    global time
    New = []
    now = time[x]
    for d in dic[x]:
        a, b, t, k = abtk[d]
        if a != x:
            next = a
        else:
            next = b

        if now % k == 0:
            go = now
        else:
            go = (now//k+1)*k

        if time[next] > go+t and time[y] > go+t:
            time[next] = go+t
            New.append(next)

    for n in New:
        dp(n)


dp(x)

if time[y] == inf:
    print(-1)
else:
    print(time[y])
