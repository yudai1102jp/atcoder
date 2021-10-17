
N, Q = map(int, input().split())
x = [0]*N
y = [0]*N
where = [0]*N
center = [0, 0]
for n in range(N):
    x[n], y[n] = map(int, input().split())
    center[0] += y[n]
    center[1] += x[n]
center[0] //= n
center[1] //= n
Max_dist = [0]*4
for n in range(N):
    y[n] -= center[0]
    x[n] -= center[1]
    dist = abs(x[n])+abs(y[n])
    if y[n] >= 0 and x[n] >= 0:  # 第一象限
        where[n] = 0
        Max_dist[0] = max(Max_dist[0], dist)
    elif y[n] >= 0 and x[n] < 0:  # 第2象限
        where[n] = 1
        Max_dist[1] = max(Max_dist[1], dist)
    elif y[n] < 0 and x[n] < 0:  # 第3象限
        where[n] = 2
        Max_dist[2] = max(Max_dist[2], dist)
    elif y[n] < 0 and x[n] >= 0:  # 第4象限
        where[n] = 3
        Max_dist[3] = max(Max_dist[3], dist)

    else:
        print('e')
for i in range(Q):
    q = int(input())
    ans = max(ans, Max_dist[(where[q]+2) % 4] + x[q]+y[q])
print(ans)
