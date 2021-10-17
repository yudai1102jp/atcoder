N, M, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [0]*S

Sum = [0]*N
Sum[-1] = A[-1]
for i in reversed(range(N-1)):
    Sum[i] = Sum[i+1]+A[i]

max_id = -1
max_val = 0
now = S
now_id = 0
s = [0]*N
while now > 0:
    for j in range(now_id, N):
        len = now-j
        if Sum[i]/len > max_val:
            max_val = Sum[i]/len
            max_id = j
    if now/(N-j) < M:
        s[j] = now/(N-j)
        now = 0
    else:
        s[j] = M
        now -= M*(N-j)

    now_id = j+1
ans = 0
now = 0
for i in range(N):
    now += s[i]

    ans += A[i]*now
print(ans)
