n = input()

len = 0

ndic = {1: 0, 2: 0, 0: 0}
for i in n:
    j = int(i)
    len += 1

    ndic[j % 3] += 1


if ndic[1] and ndic[2]:
    print(abs((ndic[1]-ndic[2])) % 3)
else:
    a = (ndic[1] % 3)+(ndic[2] % 3)
    if len == a:
        print(-1)
    else:
        print(a % 3)

print(abs(0))
