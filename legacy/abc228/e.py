import sys  # 追加
sys.setrecursionlimit(500*500)


MOD = 998244353


N, K, M = list(map(int, input().split()))
if M % MOD == 0:
    print(0)
    exit()


print(pow(M, pow(K, N, MOD-1), MOD))
