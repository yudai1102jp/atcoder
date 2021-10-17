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

ch = int(N//3)
xyr[:ch] = sort_r(xyr[:ch], 2)

ans = [[]]*N
for i in range(N):
    x, y = xyr[i][:2]
    ans[i] = [x, y, x+1, y+1]


def S(xyxy):
    return (xyxy[2]-xyxy[0])*(xyxy[3]-xyxy[1])


def score(n):
    li = xyr[n]
    x1, y1, x2, y2 = ans[n]
    s = S(ans[n])
    if (x1 < li[0] and li[0] < x2 and y1 < li[1] and li[1] < y2):

        return 1-(1-(min([li[2], s])/float(max(li[2], s))))**2
    return 0


def S_check(xyx2y2, n, Threshold):

    if Threshold*xyr[n][2] > S(xyx2y2):
        return True
    return False


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
    if tx2 <= x1 or ty2 <= y1 or tx1 >= x2 or ty1 >= y2:
        return False
    return True


def check_range(li):
    if 0 > li[0] or 0 > li[1] or 10000 < li[2] or 10000 < li[3]:
        return True
    return False

#                                 S_check


def expend(diction: list, n: int, Threshold: int = 1) -> list:
    dic = list(diction)
    ok = sum([1 for i in dic if i])
    xyx2y2 = list(ans[n])  # min  ok

    min = [0, 0, 0, 0]     #
    max = list(dic)     #
    n_xyx2y2 = [xyx2y2[i]+max[i] for i in range(4)]  # max  ok?
    flag = False   # if max ok ->true   max not ok  ->false
    while True:
        if flag:
            que = [min[i]+(max[i] - min[i])//2 if i < 2 else min[i] +
                   (max[i] - min[i]+1)//2 for i in range(4)]
            n_xyx2y2 = [xyx2y2[i]+que[i] for i in range(4)]
            if (S_check(n_xyx2y2, n, Threshold)) and check(n, n_xyx2y2):  # max ok
                min = list(que)
            else:
                max = list(que)
            if diff(min, max) is False:
                if not S_check([xyx2y2[i]+max[i] for i in range(4)], n, Threshold):
                    return [xyx2y2[i]+min[i] for i in range(4)]
                for k in check_direction(n, [xyx2y2[i]+max[i] for i in range(4)]):
                    ok -= 1
                    xyx2y2[k] += min[k]
                    min[k] = 0
                    max[k] = 0
                    flag = False
                    n_xyx2y2 = [xyx2y2[i]+max[i] for i in range(4)]
            if ok <= 0:
                break
        else:
            if (S_check(n_xyx2y2, n, Threshold)) and check(n, n_xyx2y2):  # max ok
                min = list(max)
                max = [max[i]*2 for i in range(4)]
                n_xyx2y2 = [xyx2y2[i]+max[i] for i in range(4)]
            else:
                flag = True

    return xyx2y2


def diff(min, max):
    for i in range(4):
        if abs(max[i]-min[i]) > 1:
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
    if tx1 <= x1:
        if tx2 == x1+1:
            if ty1 < y2 and ty2 > y1:
                dic.add(0)
    if ty1 <= y1:
        if ty2 == y1+1:
            if tx1 < x2 and tx2 > x1:
                dic.add(1)

    if tx2 >= x2:
        if tx1 == x2-1:
            if ty1 < y2 and ty2 > y1:
                dic.add(2)
    if ty2 >= y2:
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


def Pro_small(ch, Th):
    global ans
    for i in range(ch):
        ans[i] = expend([-1, -1, 1, 1], i, Th)


def Pro_side(Threshold, Th):

    global ans
    for i in range(N):
        expand = [0, 0, 0, 0]
        x, y = xyr[i][:2]
        if x < Threshold:
            expand[0] = -1
        elif x > 10000-Threshold:
            expand[2] = 1
        if y < Threshold:
            expand[1] = -1
        elif y > 10000-Threshold:
            expand[3] = 1
        if sum([1 for i in expand if i]):
            ans[i] = expend(expand, i, Th)


def main(Th):
    global ans
    for i in range(N):
        ans[i] = expend([-1, -1, 1, 1], i, Th)


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


# Th = {0.5:0.2929,0.8: 0.5528, 0.85: 0.6128, 0.9: 0.6838, 0.95: 0.7764}
Th = [0.0001, 0.0514, 0.1056, 0.1634, 0.2255, 0.2929, 0.3676, 0.4523, 0.5528, 0.6838]


for i in Th:
    main(i)
    Pro_side(1000, i)
    # Pro_small(ch, i)
main(1)


# for i in range(50):
#     if xyr[i][3] == 22:
#         a = i
#     if xyr[i][3] == 12:
#         b = i

# ans[b] = expend([-1, -1, 1, 1], b)
# ans[a] = expend([-1, -1, 1, 1], a)

pri()

# Time()
# s_pri([14, 42, 97, 73, 75])
