N, K_ori = map(int, input().split())
c_ori = list(map(int, input().split()))


def bikkuri(n):
    if n == 1 or n == 0:
        return 1
    return (n*bikkuri(n-1))


def co(li, n):
    a = bikkuri(n-1)
    b = 1
    s = 0
    for i in range(9):
        if li[i] != 0:
            b *= bikkuri(li[i])
            # one = one*10+1
    return a//b
