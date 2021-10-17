n = int(input())

A = []
dic = {i: 0 for i in range(1, 400000+1)}
select = {i: -1 for i in range(1, 400000+1)}
select_count = 0
for i in range(n):
    a, b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1
    A.append([a, b])
for i in range(n):
    a = A[i][0]
    b = A[i][1]
    if dic[a] == 1:
        select[a] = 0
    elif dic[b] == 1:
        select[b] = 1

