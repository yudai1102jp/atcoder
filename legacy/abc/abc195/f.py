import math

a, b = map(int, input())

primary = [2, 3, 5, 7]


if a-b == 0:
    print(2)
elif b-a == 1:
    print(1+2+1)
else:
    ans = b-a+2
    odd = 0

    Pri_n = []
    free = 0
    for i in range(a, b+1):
        temp = []
        for p in primary:
            if i % p:
                temp.append(p)
        if temp:
            Pri_n.append(temp)
        else:
            free += 1
