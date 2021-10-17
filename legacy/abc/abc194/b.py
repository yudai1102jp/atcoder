n = int(input())


ab = [[int(i) for i in input().split()] for j in range(n)]

af = [1000000, 0]
As = [1000000, 0]
bf = [1000000, 0]
bs = [100000000, 0]
for i in range(n):

    a, b = ab[i][0], ab[i][1]

    if a < af[0]:
        As = af
        af = [a, i]

    elif a < As[0]:
        As = [a, i]
    if b < bf[0]:
        bs = bf
        bf = [b, i]

    elif b < bs[0]:
        bs = [b, i]


if af[1] == bf[1]:
    ff = af[0]+bf[0]
    fs = max([af[0], bs[0]])
    sf = max([bf[0], As[0]])
    temp = min([ff, fs, sf])
    print(temp)
else:
    print(max([af[0], bf[0]]))
