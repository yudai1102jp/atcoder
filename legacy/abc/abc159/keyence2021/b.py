import collections

n,k=list(map(int,input().split()))
a=collections.Counter(list(map(int,input().split())))

b={i:0 for i in range(n+2)}

b.update(dict(a))



last=k
ans=0
for key,value in b.items():
    if value <last:
        ans+=(last-value)*key
        last=value
     
    if not value:
        break

print(ans)