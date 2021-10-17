import math
import numpy as np
N, K = map(int, input().split())

lis = np.array([0]*(N+1))
ans = 0
if K == 1:
    print(N-1)
    exit()

for odd in range(2, N+1, 2):
    lis[odd] += 1
for p in range(3, N//2+1, 2):
    if lis[p] != 0:
        continue
    for odd in range(p, N+1, p):
        lis[odd] += 1

for i in lis:
    if i >= K:
        ans += 1

print(ans)
