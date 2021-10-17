import sys
sys.setrecursionlimit(10**6)


N = int(input())
allow = [[] for i in range(N+5)]

for i in range(N-1):
    A, B = map(int, input().split())
    allow[A-1].append(B-1)
    allow[B-1].append(A-1)

Max = [0, 0]


def treeDFS(From, now, dist):
    global Max
    if dist > Max[1]:
        Max = [now, dist]
    for next in allow[now]:
        if next == From:
            continue
        treeDFS(now, next, dist+1)


treeDFS(-1, 0, 0)
start = Max[0]
Max = [0, 0]
treeDFS(-1, start, 0)
print(Max[1]+1)
