import numpy as np
N, K = input().split()
K = int(K)

new_N = []
for i in range(K):
    S = np.base_repr(int(N, 8), 9)
    new = []
    for s in S:
        new.append(s if s != '8' else '5')
    N = ''.join(new)
print(N)
