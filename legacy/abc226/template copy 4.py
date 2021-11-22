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
a = list(input())
N = int(input())
A = list(map(int, input().split()))
A = [[int(i) for i in input().split()] for j in range(N)]
