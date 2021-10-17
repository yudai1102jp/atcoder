import math
from sys import stdin
import time
start = time.time()
input = stdin.readline


def sort_r(li, sort_num=0):
    re_li = list(li)

    for i in range(len(li)):
        re_li[i][0], re_li[i][sort_num] = re_li[i][sort_num], re_li[i][0]
    re_li.sort()

    for i in range(len(li)):
        re_li[i][0], re_li[i][sort_num] = re_li[i][sort_num], re_li[i][0]

    return re_li


N = int(input())

xyr = [[int(i) for i in input().split()] for j in range(N)]
for i in range(N):
    xyr[i].append(i)

ch = int(N)
xyr[:ch] = sort_r(xyr[:ch], 2)

ans = [[]]*N
for i in range(N):
    x, y = xyr[i][:2]
    ans[i] = [x, y, x+1, y+1]


def S(x1, y1, x2, y2):
    return (x2-x1)*(y2-y1)


def score(n):
    li = xyr[n]
    x1, y1, x2, y2 = ans[n]
    s = S(*ans[n])
    if (x1 < li[0] and li[0] < x2 and y1 < li[1] and li[1] < y2):

        return 1-(1-(min([li[2], s])/float(max(li[2], s))))**2
    return 0


def S_check(x1, y1, x2, y2, r):
    Threshold = 0.7764  # p>=0.9 -> 0.6838  ,   p>=0.95 -> 0.7764  ,
    if Threshold*r > (x2-x1)*(y2-y1):
        return False
    return True


def check(n, li):
    if check_range(li):
        return False
    for i in range(N):
        if i == n:
            continue
        if check1(*li, *ans[i]):
            return False

    return True


def check1(x1, y1, x2, y2, tx1, ty1, tx2, ty2):
    if tx2 < x1 or ty2 < y1 or tx1 > x2 or ty1 > y2:
        return False
    return True


def check_range(li):
    if 0 > li[0] or 0 > li[1] or 10000 < li[2] or 10000 < li[3]:
        return True
    return False


def check_direction(n, li):
    dic = check_direction_range(li)
    if dic:
        return dic
    for i in range(N):
        if i == n:
            continue
        dic = check1_direc(*li, *ans[i])
        if dic:
            return dic

    return set()  # 0 x1 , 1 y1 , 2 x2 , 3 y2


def check1_direc(x1, y1, x2, y2, tx1, ty1, tx2, ty2):
    if tx2 <= x1 or ty2 <= y1 or tx1 >= x2 or ty1 >= y2:
        return False
    dic = set()
    if tx1 < x1:
        if tx2 == x1+1:
            if ty1 < y2 and ty2 > y1:
                dic.add(0)
    if ty1 < y1:
        if ty2 == y1+1:
            if tx1 < x2 and tx2 > x1:
                dic.add(1)

    if tx2 > x2:
        if tx1 == x2-1:
            if ty1 < y2 and ty2 > y1:
                dic.add(2)
    if ty2 > y2:
        if ty1 == y2-1:
            if tx1 < x2 and tx2 > x1:
                dic.add(3)
    if dic:
        return dic
    else:
        return set([0, 1, 2, 3])


def check_direction_range(li):
    dic = set()
    for i in range(4):
        if i < 2:
            if 0 > li[i]:
                dic.add(i)
        else:
            if 10000 < li[i]:
                dic.add(i)

    return dic  # 0 x1 , 1 y1 , 2 x2 , 3 y2


# def convert_dic(dic):
#     li = [0, 0, 0, 0]
#     if 0 in dic:
def Preprocessing(ch, sh):
    Pro_small()
    Pro_side(ch, sh)


def Pro_small():
    global ans
    for i in range(ch):
        x1, y1, x2, y2 = ans[i]
        xyx2y2 = ans[i]
        expand = [-1, -1, 1, 1]
        ok = 4
        while (not S_check(*xyx2y2, xyr[i][2])) and ok > 0:
            n_xyx2y2 = list(xyx2y2)
            for j in range(4):
                n_xyx2y2[j] += expand[j]
            dic = check_direction(i, n_xyx2y2)
            if dic:
                for j in dic:
                    expand[j] = 0
                    ok -= 1
            else:
                xyx2y2 = n_xyx2y2
        ans[i] = xyx2y2


def Pro_side(ch, Threshold):

    global ans
    for i in range(ch, N):
        x1, y1, x2, y2 = ans[i]
        xyx2y2 = ans[i]
        expand = [0, 0, 0, 0]
        ok = 0

        for dic in range(4):
            if dic < 2:
                if xyx2y2[dic] < Threshold:
                    expand[dic] = -1
                    ok += 1
            else:
                if xyx2y2[dic] > 10000-Threshold:
                    expand[dic] = 1
                    ok += 1

        while (not S_check(*xyx2y2, xyr[i][2])) and ok > 0:
            n_xyx2y2 = list(xyx2y2)
            for j in range(4):
                n_xyx2y2[j] += expand[j]
            dic = check_direction(i, n_xyx2y2)
            if dic:
                for j in dic:
                    expand[j] = 0
                    ok -= 1
            else:
                xyx2y2 = n_xyx2y2
        ans[i] = xyx2y2


def main(ch):
    global ans
    for i in range(ch, N):
        x1, y1, x2, y2 = ans[i]
        xyx2y2 = ans[i]
        expand = [-1, -1, 1, 1]
        ok = 4
        while (not S_check(*xyx2y2, xyr[i][2])) and ok > 0:
            n_xyx2y2 = list(xyx2y2)
            for j in range(4):
                n_xyx2y2[j] += expand[j]
            dic = check_direction(i, n_xyx2y2)
            if dic:
                for j in dic:
                    expand[j] = 0
                    ok -= 1
            else:
                xyx2y2 = n_xyx2y2
        ans[i] = xyx2y2


def pri():
    for j in re_sort(ans):
        print(' '.join([str(i) for i in j]))


def re_sort(li):
    new_ans = [[]]*N
    for i in range(N):
        new_ans[xyr[i][3]] = li[i]
    return new_ans


def s_pri(li):
    for n in li:
        print()
        x, y, r, i = xyr[n]
        x1, y1, x2, y2 = ans[n]
        print(f"num {n}")
        print(f"x = {x} ,  y = {y} ,  r = {r}")
        print("x1 = {} ,  y1 = {} ,  x2 = {} ,  y2 = {}".format(x1, y1, x2, y2))
        print(f"S = {(x2-x1)* (y2-y1) }")
        print(f"aspect = {(x2-x1)* (y2-y1)/r}")
        print(f"score = {score(n)}")
        print()


def Time():
    print()
    print(f"time {time.time()-start}s")
    print()


Preprocessing(ch, 1500)
main(ch)
pri()
Time()
# for i in range(10):
s_pri([14, 42, 97, 73, 75])
