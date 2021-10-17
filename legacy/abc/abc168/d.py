n, m = map(int, input().split())


load = {i: [] for i in range(1, n+1)}
point = {i: 0 for i in range(2, n+1)}
new_list = []
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        point[b] = 1
        new_list.append(b)
    elif b == 1:
        point[a] = 1
        new_list.append(a)

    else:
        load[a].append(b)
        load[b].append(a)


serch_list = []
while True:

    serch_list = list(new_list)
    new_list = []

    for i in serch_list:
        for j in load[i]:

            if not point[j]:
                point[j] = i
                new_list.append(j)

    if not new_list:
        break


if 0 in point.values():
    print("No")
else:
    print("Yes")
    for i in point.values():
        print(i)
