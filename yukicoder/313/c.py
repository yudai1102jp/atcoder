N = int(input())
A = list(map(int, input().split()))
bit = [1]*64
for i in range(N):
    a = A[i]
    now = 0
    for b in range(64):
        if bit[b] and (a >> b) & 1:
            bit[b] = 0

for b in range(64):
    if bit[b]:
        print(1 << b)
        break
