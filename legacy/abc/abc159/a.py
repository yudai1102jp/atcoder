n, m = map(int,input().split())


ans=0
for i in range(n):
    ans+=i
for i in range(m):
    ans+=i

print(ans)
