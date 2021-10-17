a, b, c = map(int, input().split())

k = int(input())
p = 10**9+7
x = pow(2, k, p-1)


ans = pow(a, x, p)*pow(b, x, p)*pow(c, x, p)
print(ans % p)
