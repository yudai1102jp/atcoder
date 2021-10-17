n = int(input())
li = list(map(int, input().split()))


ans = 0
ansmax = 0

for i in range(2, max(li)+1):

    count = 0
    for j in li:
        if j % i == 0:
            count += 1
    if ansmax < count:
        ansmax = int(count)
        ans = i
print(ans)
