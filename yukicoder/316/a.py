N, M = map(int, input().split())
A = list(map(int, input().split()))
Max = N
dp = [0]*(M+1)
for i in range(N):
    if dp[A[i]-1]:
        Max -= 1
    dp[A[i]-1] += 1
if len(set(A)) == 1 and N == M:
    Min = 1
else:
    Min = 0

print(f'{Max} {Min}')
