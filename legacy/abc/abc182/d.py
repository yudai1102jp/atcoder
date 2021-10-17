n = int(input())

li = list(map(int, input().split()))


now = 0

maxnow = 0

ans = 0

d = []

for i in range(0, n):
    if i :
        d.append(d[-1]+li[i])
    else:
        d.append(li[i])
    maxnow = max([maxnow, d[-1]])
    ans = max([ans,now+maxnow])
    now += d[-1]

print(ans)
