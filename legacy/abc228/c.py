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


# MOD = int(1e9+7)
# a = list(input())
# N = int(input())
N, K = list(map(int, input().split()))
P = [sum([int(i) for i in input().split()]) for j in range(N)]
K_test = sorted(P, reverse=True)

K_point = 12000

for i in range(N):
    if K_test[i] < K_point:
        K_point = K_test[i]

    if K == i+1:
        break

for i in range(N):
    if P[i]+300 >= K_point:
        print('Yes')
    else:
        print('No')
