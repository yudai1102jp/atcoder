N, Q = map(int, input().split())
A = list(map(int, input().split()))

Txy = [[int(i) for i in input().split()] for j in range(Q)]


roll = 0
for i in range(Q):
    T, x, y = Txy[i]
    if T == 1:
        x = (x-roll-1+N) % N

        y = (y-roll-1+N) % N
        A[x], A[y] = A[y], A[x]

    elif T == 2:
        roll += 1
        roll %= N
    else:
        print(A[((x-roll-1+N) % N) % N])
