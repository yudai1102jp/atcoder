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


N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

flag = [0]*(N+1)

now = X
while True:
    if flag[now]:
        break
    flag[now] = 1
    now = A[now-1]


print(sum(flag))
