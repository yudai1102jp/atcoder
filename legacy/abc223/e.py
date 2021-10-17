# a = list(input())
import itertools

X, Y, A, B, C = list(map(int, input().split()))
# A=[[int(i) for i in input().split()] for j in range(N)]

A1, A2, A3 = sorted((A, B, C))
X1, Y1 = sorted((X, Y))


def check(a, b, c, X, Y):
    y = (a+X-1)//X
    x = (a+X-1)//y
    if X-x > b//Y+1:

        if (X-((b+Y-1)//Y))*(Y-y) >= c:
            return True
        else:
            if (X-(x)-((b+Y-1)//Y))*(Y) >= c:
                return True
    else:
        bx = (b+Y-y-1)//(Y-y)
        if (X-bx)*(Y-y) >= c:
            return True
        elif Y*(X-x) >= c:
            return True
        by = y+(b+X-1)//X
        if (Y-by)*X >= c:
            return True
    return False


if X1 == 1:
    if A1+A2+A3 <= Y1:
        print('Yes')
    else:
        print('No')
elif A+B+C > X*Y:
    print('No')
else:

    for a, b, c in itertools.permutations((A, B, C), 3):
        for x, y in itertools.permutations((X, Y), 2):
            if check(a, b, c, x, y):
                print('Yes')
                exit()
    else:
        print('No')
