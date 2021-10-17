
n, m = map(int, input().split())
a = list(map(int, input().split()))

co = [0]*n

for i in range(m):
    co[a[i]] += 1
for i in range(n):
    if not co[i]:
        ans = i
        break
else:
    ans=n


for i in range(n-m):
    co[a[i]] -= 1
    co[a[i+m]] += 1
    if co[a[i]] == 0:
        if ans > a[i]:
            ans = a[i]


print(ans)
