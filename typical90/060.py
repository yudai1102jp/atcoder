from collections import deque
from typing import Collection


N= int(input())
MOD = int(1e5) 
used = [-1]*int(1e5)
x = N
count = 0
flag = True
while count < K:
    if used[x] != -1 and flag:
        loop = count-used[x]
        count = K-(K-count) % loop
        flag = False

    else:
        used[x] = count
        y = 0
        for s in str(x):
            y += int(s)
        x = (y+x) % MOD
        count += 1
print(x)
