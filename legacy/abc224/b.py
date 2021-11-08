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
# N = int(input())
H, W = list(map(int, input().split()))
A = [[int(i) for i in input().split()] for j in range(H)]

flag = True
for i1 in range(H-1):
    for i2 in range(i1+1, H):
        for j1 in range(W-1):
            for j2 in range(j1+1, W):
                if A[i1][j1]+A[i2][j2] > A[i2][j1]+A[i1][j2]:
                    flag = False

if flag:
    print('Yes')
else:
    print('No')
