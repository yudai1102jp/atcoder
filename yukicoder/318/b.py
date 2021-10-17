N, M, X = map(int, input().split())
AB = [[int(i) for i in input().split()] for j in range(N)]

K = int(input())
C = list(map(int, input().split()))


# problem = {i+1: [] for i in range(M)}
# for i in range(N):
#     problem[AB[i][1]].append(AB[i][0])
# for i in range(M):
#     problem[i+1].sort(reverse=True)
#     problem[i+1][0] += X
Max = [-1]*M
for i in range(N):
    if Max[AB[i][1]-1] == -1 or AB[Max[AB[i][1]-1]][0] < AB[i][0]:
        Max[AB[i][1]-1] = i

for i in range(M):
    if Max[i] != -1:
        AB[Max[i]][0] += X
AB.sort(reverse=True, key=lambda x: x[0])


for i in range(1, N):
    AB[i][0] += AB[i-1][0]
ans = 0
for i in range(K):
    if C[i] > 0:
        ans += AB[C[i]-1][0]
print(ans)
