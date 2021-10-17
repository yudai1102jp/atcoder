N = int(input())

P = list(map(int, input().split()))
P_index = [[P[i], i+1] for i in range(N)]

P_index.sort(key=lambda x: x[0], reverse=True)
ans = 0
Sum = (1+N)*N//2
for i in range(N):
    ans = max(ans, Sum-2*P_index[i][1])
    Sum -= P_index[i][1]
print(ans)
