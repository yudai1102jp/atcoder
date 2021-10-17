import numpy as np
def score(s, si):
    return 1-(1-(min([s, si])/float(max(s, si))))**2


def get_Th():
    s = 10000
    Th = 0.85
    TH = [(int(i))/10.0 for i in range(10)]

    print("Th=[", end='')

    for Th in TH:
        for i in range(s):
            if score(s, i) > Th:
                if Th == TH[-1]:
                    print(f"{i/float(s)}", end='')
                else:
                    print(f"{i/float(s)},", end='')
                break
    print("]")


def anarisice():
    N = int(input())
    ans = [0]*N
    for i in range(N):
        ans[i] = int(input())

    print("平均値:", np.mean(ans))
    print("標準偏差:", np.std(ans))
    print("中央値:", np.median(ans))
    print("最小値:", np.min(ans))
    print("最大値:", np.max(ans))

    print("----------------------------------")


# get_Th()
anarisice()
