import sys
sys.setrecursionlimit(10**6)  # 再帰関数使う時有効

N = int(input())
c = list(map(int, input().split()))

MOD = 10**9+7


def bikkuri(n):
    if n == 1 or n == 0:
        return 1
    return (n*bikkuri(n-1)) % MOD


a = bikkuri(N-1)
b = 1

s = 0
for i in range(9):
    if c[i] != 0:
        b *= bikkuri(c[i])
        b %= MOD
        # one = one*10+1
        s += (i+1)*c[i]

n = (a*pow(b, -1, MOD)) % MOD
n *= s
ans = 0
for i in range(N):
    ans = ans*10+n
    ans %= MOD
print(ans)
