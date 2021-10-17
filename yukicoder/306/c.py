from math import gcd

a = int(input().replace('.', ''))

g = gcd(a, 1000)

up = a//g
down = 1000//g

count = up+down-2+(up+down)//2+abs(up-down)//2


if (up+down) % 2 == 0:
    print(f'A {count}')
elif up % 2 == 0:
    print(f'B {count}')
else:
    print(f'C {count}')
