N = int(input())
A = list(map(int, input().split()))

ans = 0
MOD = 998244353
ans = 0
for i in range(N-1):
    for j in range(1, N):
