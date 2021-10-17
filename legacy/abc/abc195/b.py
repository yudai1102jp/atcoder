a, b, w = map(int, input().split())
w


def check():

    n = (w*1000)//a
    if w*1000 <= b*n:
        return True
    return False


if check():
    if (w*1000) % b == 0:
        print((w*1000)//b, end=' ')
    else:
        print((w*1000)//b+1, end=' ' )

    print((w*1000)//a)


else:
    print("UNSATISFIABLE")
