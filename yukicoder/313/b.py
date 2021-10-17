N, Q = map(int, input().split())
LR = [[int(i) for i in input().split()] for j in range(Q)]

state = [False]*N
now = 0

for q in range(Q):
    l, r = LR[q]

    for i in range(l-1, r):
        if state[i]:
            state[i] = False
            now -= 1
        else:
            state[i] = True
            now += 1
    print(now)
