N = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        if P[i] > P[j]:
            P[j] += 1
    ans += P[i]-i-1
print(ans)
