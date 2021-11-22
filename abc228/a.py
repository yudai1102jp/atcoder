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

# N = int(input())
S, T, X = list(map(int, input().split()))
# A = [[int(i) for i in input().split()] for j in range(N)]
if S > T:
    if T <= X and X < S:
        print('No')
    else:
        print('Yes')

else:
    if S <= X and X < T:
        print('Yes')
    else:
        print('No')
