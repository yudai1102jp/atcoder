import sys  # 追加
sys.setrecursionlimit(500*500)


def YES():
    print('Yes')


def NO():
    print('No')


def TAKAHASHI():
    print('Takahashi')


def AOKI():
    print("Aoki")


N = int(input())
# A = list(map(int, input().split()))
ab = [[int(i) for i in input().split()] for j in range(N-1)]

if N == 3:
    print('Yes')
    exit()

load = [[] for i in range(N)]
for i in range(N-1):
    load[ab[i][1]-1].append(ab[i][0]-1)
    load[ab[i][0]-1].append(ab[i][1]-1)
flag = -1
for i in range(N):
    if len(load[i]) > 1:
        flag = i
        break
if flag == -1:
    print('No')
else:
    for i in range(N):
        if i == flag:
            continue
        if len((load[i])) == 1 and load[i][0] == flag:
            continue
        print('No')
        exit()
    print('Yes')
