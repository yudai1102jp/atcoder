from collections import deque

Q = int(input())
tx = [[int(i) for i in input().split()] for j in range(Q)]


dec = deque([])
for t, x in tx:
    if t == 1:
        dec.appendleft(x)
    elif t == 2:
        dec.append(x)
    else:
        print(dec[x-1])
