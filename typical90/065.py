N = int(input())
LR = [[int(i) for i in input().split()] for j in range(N)]
ans = 0.0
for n in range(1, N):
    nowl, nowr = LR[n]
    for i in range(n):
        co = 0
        for now in range(nowl, nowr+1):
            l, r = LR[i]
            co += len([j for j in range(l, r+1) if j > now])
        ans += co/((r-l+1)*(nowr-nowl+1))

print(ans)
