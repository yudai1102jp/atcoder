import sys  # 追加
sys.setrecursionlimit(500*500)
Inf = 2e9
N = int(input())
xy = [[int(i) for i in input().split()] for j in range(N)]


angurarcheck = [[0, 0] for i in range(N)]
angurar = [[0, i//2] for i in range(2*N)]

for i in range(N):
    if xy[i][0] == 1:
        angurarcheck[i][1] = Inf
        angurar[2*i] = [Inf, i]
    else:
        now = xy[i][1]/(xy[i][0]-1)
        angurar[2*i] = [now, i]
        angurarcheck[i][1] = now

    now = (xy[i][1]-1)/(xy[i][0])
    angurar[2*i+1] = [now, i]
    angurarcheck[i][0] = now

ans = 0
last_time = 0
angurarcheck.sort(key=lambda x: x[1])
for i in range(N):
    if last_time <= angurarcheck[i][0]:
        ans += 1
        last_time = angurarcheck[i][1]


print(ans)
