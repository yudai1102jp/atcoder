n=int(input())
apx=[[int(i) for i in input().split()] for _ in range(n)]

ans=10000000000000000
for a, p, x in apx:
    if (x-(a))>0:
        ans=min(ans,p)

if ans == 10000000000000000:
    print(-1)
else:
    print(ans)
