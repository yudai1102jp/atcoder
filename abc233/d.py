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


N, K = na()
A = na()

tail = 0
top = 1
now = A[0]
ans = 0

Sum = [0]*N
Sum[0] = A[0]
Dic = {Sum[0]: [0]}
if Sum[0] == K:
    ans = 1
for i in range(1, N):
    Sum[i] = Sum[i-1]+A[i]
    if Sum[i] in Dic:
        Dic[Sum[i]].append(i)
    else:
        Dic[Sum[i]] = [i]


for i in range(1, N):
    if Sum[i] == K:
        ans += 1
    if Sum[i]-K in Dic:
        check = Dic[Sum[i]-K]
        if check[0] < i:
            ok = 0
            ng = len(check)

            while ng-ok != 1:
                now = (ok+ng)//2
                if check[now] < i:
                    ok = now
                else:
                    ng = now
            ans += ok+1


print(ans)
