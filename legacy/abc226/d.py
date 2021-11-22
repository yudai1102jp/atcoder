import math
import sys  # 追加
sys.setrecursionlimit(500*500)
keta = 10**9+1


def YES():
    print('Yes')


def NO():
    print('No')


def TAKAHASHI():
    print('Takahashi')


def AOKI():
    print("Aoki")


MOD = int(1e9+7)
N = int(input())
xy = [[int(i) for i in input().split()] for j in range(N)]


remind = set()
ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        movex = xy[i][0]-xy[j][0]
        movey = xy[i][1]-xy[j][1]
        Gcd = math.gcd(movex, movey)

        move = (movex//Gcd)*keta+movey//Gcd
        if move not in remind:
            remind.add(move)
            ans += 1

        if -move not in remind:
            remind.add(-move)
            ans += 1
print(ans)
