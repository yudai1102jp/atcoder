import math
a1 = 32134
b1 = 1584891

a2 = 193127
b2 = 3438478

n = 1


def cal(a, b,):  # 拡張ユークリッド互助法（不定１次方程式の特殊解）　// ax + by = gcd(a, b)

    if (b == 0):
        x = 1
        y = 0
        return a, y, x

    d, x1, y1 = cal(b, a % b)
    y1 -= a//b * x1
    return d, y1, x1


a, y1, x1 = (cal(b1, b2))
print(x1, y1)
# a, x1, y1 = (cal(b1, -1*b2))

x1 *= (a2-a1)*math.gcd(b1, b2)
y1 *= (a2-a1)*math.gcd(b1, b2)


x = b1*x1
print(x)

print(x % b1 == a1)

print(x % b2 == a2)


print(f"x1*b1+y1*b2={x1*b1+y1*b2}")
m = y1*-1
print(f"n*b1-m*b2={x1*b1-m*b2}")
print(f"a2-a1={a2-a1}")
print(x1*b1+y1*b2 == a2-a1)
print("cpaw{", x1*b1+a1, "}")
print("cpaw{", -1*(y1)*b2+a2, "}")
d = math.gcd(b1, b2)
a_ = b1//d
b_ = b2//d

x = x1+b_
y = y1-a_
print(x1-b_)
print(y1+a_)
print(x*b1+y*b2 == a2-a1)
i = 0
x=x1
y=y1
while x*b1+a1 < 0:

    x = x1-b_*i
    y = y1+a_*i
    i -= 1
    if (i%10000)==0:
        print(x*b1+y*b2 == a2-a1)
        print("cpaw{", x*b1+a1, "}")
        print("cpaw{", -1*(y)*b2+a2, "}")

print(x*b1+y*b2 == a2-a1)
print("cpaw{", x*b1+a1, "}")
print("cpaw{", -1*(y)*b2+a2, "}")
