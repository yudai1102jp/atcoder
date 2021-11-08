import heapq
H, W, N = list(map(int, input().split()))
rca = [[int(i) for i in input().split()] for j in range(N)]
for i in range(N):
    rca[i].append(i)
rca_sort = sorted(rca, key=lambda x: x[0])

dict_y = {}
dict_y_rev = {}
y = [heapq.heapify([]) for i in range(H+1)]
now = 0
dict_y = {rca_sort[i][0]: now}
dict_y_rev = {now: rca_sort[i][0]}
heapq.heappush(y[now], rca_sort[i][3])
for i in range(1, H):
    if rca_sort[i][0] != rca_sort[i-1][0]:

        now += 1
        dict_y = {rca_sort[i][0]: now}
        dict_y_rev = {now: rca_sort[i][0]}
    heapq.heappush(y[now], rca_sort[i][3])

rca_sort = sorted(rca, key=lambda x: x[1])

x = [heapq.heapify([]) for i in range(W+1)]
now = 0
dict_x = {rca_sort[i][1]: now}
dict_x_rev = {now: rca_sort[i][1]}
heapq.heappush(x[now], rca_sort[i][3])
for i in range(1, W):
    if rca_sort[i][1] != rca_sort[i-1][1]:

        now += 1
        dict_x = {rca_sort[i][1]: now}
        dict_x_rev = {now: rca_sort[i][1]}
    heapq.heappush(y[now], rca_sort[i][3])

rca_sort = sorted(rca, reverse=True, key=lambda x: x[2])
ans = [-1]*N
add_y=[]
ans[rca_sort[3]] = 0
for i in range(N):
    ans[ rca_sort[]]
