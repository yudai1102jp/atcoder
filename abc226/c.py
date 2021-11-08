import sys  # 追加
sys.setrecursionlimit(500*500)

N = int(input())
TKA = [[int(i) for i in input().split()] for j in range(N)]
ok = set()


def syutoku(n, t):
    global ok
    for i in range(TKA[n][1]):
        if TKA[n][2+i]-1 in ok:
            continue
        t = syutoku(TKA[n][2+i]-1, t)
    t += TKA[n][0]
    ok.add(n)
    return t


print(syutoku(N-1, 0))
