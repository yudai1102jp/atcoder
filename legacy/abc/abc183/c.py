n, k = map(int, input().split())


sig = 0
for i in range(2, n):
    sig *= i
t = [list(map(int, input().split())) for i in range(n)]


timesun = []
li = []


def new_row(lis, lis2):
    
    now_li = list(lis)
    for i in lis2:
        se=[j for j in list(lis2) if i !=j]
      
        if se:
            new_row(now_li+[i], se)
        else:
            global li
            li.append([1]+now_li+[i, 1])


co = 1

lis = [i for i in range(2, n+1)]
new_row([], lis)
ans = 0
for i in li:
    pre = 1
    time = 0
    for j in i[1:]:
        time += t[pre-1][j-1]
        pre = j

    if time == k:
        ans += 1

print(ans)
