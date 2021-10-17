# a=map(int, input().split())
import itertools

N = [int(i) for i in input()]


def conv(a):
    l = len(a)
    if l == 1:
        return int(a[0])
    ans = 0
    for i in range(l):
        ans += pow(10, i)*a[l-1-i]
    return ans


ans = 0
for i in range(1, 2**len(N)-1):
    a = []
    b = []

    for j in range(len(N)):
        if i & 1 << j:
            a.append(N[j])
        else:
            b.append(N[j])
    if sum(a) == 0 or sum(b) == 0:
        continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = max(ans, conv(a)*conv(b))


print(ans)
