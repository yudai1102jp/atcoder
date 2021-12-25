import math
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
N, X = na()
LA = [na() for i in range(N)]


def cal(raw, num):
    La = LA[raw-1]
    count = 0
    if raw == N:
        for i in range(La[0]):
            if num*La[i+1] == X:
                count += 1
        return count
    for i in range(La[0]):
        count += cal(raw+1, num*La[i+1])
    return count


print(cal(1, 1))
