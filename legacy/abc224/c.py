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


MOD = int(1e9+7)
# a = list(input())
N = int(input())
# XY = list(map(int, input().split()))
XY = [[int(i) for i in input().split()] for j in range(N)]
ans = 0
for i in range(N-2):
    for j in range(i, N-1):
        for k in range(j, N):
            if XY[i][0] == XY[j][0] == XY[k][0]:
                continue
            if XY[i][1] == XY[j][1] == XY[k][1]:
                continue
            if (XY[k][1]-XY[i][1])*(XY[j][0]-XY[i][0]) == (XY[j][1]-XY[i][1])*(XY[k][0]-XY[i][0]):
                continue
            ans += 1

print(ans)
