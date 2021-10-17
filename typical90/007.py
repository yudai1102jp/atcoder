N = int(input())
A = [0] * (N+2)
A[0] = -1e11
A[N+1] = 1e11+5
A[1:N+1] = [int(i) for i in input().split()]

Q = int(input())


A.sort()

for i in range(Q):
    ok = 0
    ng = N+1
    B = int(input())
    while ok+1 != ng:
        now = (ok+ng)//2
        if A[now] < B:
            ok = now
        else:
            ng = now

    print(min(B-A[ok], A[ng]-B))
