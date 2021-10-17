import math
A, B = map(int, input().split())

a = math.gcd(A, B)
b = max(A, B)//a*min(A, B)

print(b if b <= 1e18 else "Large")
