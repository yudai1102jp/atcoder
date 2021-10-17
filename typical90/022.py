import math
a, b, c = map(int, input().split())


g = math.gcd(math.gcd(a, b), c)
a = a//g
b = b//g
c = c//g

print(a+b+c-3)
