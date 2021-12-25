
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


X = ns()


Sum = sum(map(int, list(X)))
ans = []
lenX = len(X)

kuriage = Sum
now = 0
while now <= lenX or kuriage != 0:
    if now == 0:
        ans.append(str(kuriage % 10))
        kuriage = kuriage//10
        now += 1
    elif now <= lenX:
        Sum -= int(X[lenX-now])
        kuriage += Sum
        ans.append(str(kuriage % 10))
        kuriage = kuriage//10
        now += 1
    else:
        ans.append(str(kuriage % 10))
        kuriage = kuriage//10

flag = True
for i in ans[::-1]:
    if flag and i != '0':
        flag = not flag
    if not flag:
        print(i, end='')
print()
