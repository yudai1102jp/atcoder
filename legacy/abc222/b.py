# a=map(int, input().split())
# a=int(input())
N, P = list(map(int, input().split()))
a = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    if a[i] < P:
        ans += 1
print(ans)
