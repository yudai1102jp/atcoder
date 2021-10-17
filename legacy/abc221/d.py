N = int(input())
AB = [[int(i) for i in input().split()] for j in range(N)]


day = []
for i in range(N):
    day.append(AB[i][0])
    day.append(AB[i][0]+AB[i][1])

day.sort()

comp = {0: 0}
index = 1
for i in range(2*N):
    if day[i] not in comp:
        comp[day[i]] = index
        index += 1

comp_rev = {v: k for k, v in comp.items()}
# for k, v in comp.items():
#     comp_rev[v] = k

l = len(comp)
dp = [0]*index
for i in range(N):
    dp[comp[AB[i][0]]] += 1
    dp[comp[AB[i][0]+AB[i][1]]] -= 1

ans = [0]*(N+5)
now = 0
passed_day = 0
for i in range(1, l):
    passed_day = comp_rev[i]-comp_rev[i-1]
    ans[now] += passed_day
    now += dp[i]

for i in range(1, N+1):
    print(ans[i])
