W, N = map(int, input().split())

LRV = [[int(i) for i in input().split()] for j in range(N)]
LRV.sort()


ok = [-1]*(W+1)
ok[0] = 0
used = [[] for i in range(W+1)]
for i in range(1, W+1):
    for j in range(N):
        L, R, V = LRV[j]
        for k in range(L, R+1):
            if i-k < 0:
                break
            if j in used[i-k] or ok[i-k] == -1:
                continue
            if ok[i] < ok[i-k]+V:
                ok[i] = ok[i-k]+V
                used[i] = used[i-k]+[j]
print(ok[-1])
