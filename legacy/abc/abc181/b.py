n=int(input())
ans=0
for i in range(n):
    n,m=map(int, input().split())
    ans+=int((n+m)*(m-n+1)/2)

print(ans) 