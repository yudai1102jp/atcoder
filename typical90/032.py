import itertools
N = int(input())
A = [[int(i) for i in input().split()] for j in range(N)]

M = int(input())

bad = [[] for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad[x].append(y)
    bad[y].append(x)

ans = 100000
for a in itertools.permutations(range(N), N):
    temp = 0
    for i in range(N-1):
        temp += A[a[i]][i]
        if a[i+1] in bad[a[i]]:
            break
        elif a[i] in bad[a[i+1]]:
            break
    else:
        ans = min(ans, temp+A[a[N-1]][N-1])
if ans == 100000:
    print(-1)
else:
    print(ans)
