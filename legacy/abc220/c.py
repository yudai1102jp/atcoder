N = int(input())

A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)

ans = (X//sumA)*N
X %= sumA
now = 0
for i in range(N):
    ans += 1
    now += A[i]
    if now > X:
        break
print(ans)
