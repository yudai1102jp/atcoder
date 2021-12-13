
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

N = ni()
S = [ns() for i in range(N)]

dic = {}
ans = ''
num = 0
for i in range(len(S)):
    if S[i] in dic:
        dic[S[i]] += 1
    else:
        dic[S[i]] = 1

    if num < dic[S[i]]:
        ans = i
        num = dic[S[i]]
print(S[ans])
