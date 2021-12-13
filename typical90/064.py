N, Q = map(int, input().split())

A = list(map(int, input().split()))
LRV = [[int(i) for i in input().split()] for j in range(Q)]

M = [A[i+1]-A[i] for i in range(N-1)]
cost = sum([abs(i) for i in M])

for i in range(Q):
    l, r, v = LRV[i]
    if 1 < l:
        cost -= abs(M[l-2])
        M[l-2] += v
        cost += abs(M[l-2])
    if r < N:
        cost -= abs(M[r-1])
        M[r-1] -= v
        cost += abs(M[r-1])
    print(cost)
