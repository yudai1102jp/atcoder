
MOD = 998244353  # type: int

n = int(input())
a = [int(i) for i in input().split()]

a.sort()


ans = 0
temp = 0
for i in range(n):
    if i:

        temp = (temp*2 + a[i-1]) % MOD
    ans += a[i]*(temp + a[i]) % MOD


print((ans) % MOD)
