
import sys  # 追加
sys.setrecursionlimit(500*500)

stdin = sys.stdin


def YES(): print('Yes')
def NO(): print('No')
def TAKAHASHI(): print('Takahashi')
def AOKI(): print("Aoki")
def ns(): return stdin.readline().strip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nz(): return list(map(lambda x: int(x)-1, stdin.readline().split()))


MOD = int(1e9+7)

N, Q = na()
A = na()

A.sort()

for i in range(Q):
    x = ni()

    Min = -1
    Max = N
    while Max-Min != 1:
        now = (Min+Max)//2
        if A[now] >= x:
            Max = now
        else:
            Min = now

    print(N-Min-1)
