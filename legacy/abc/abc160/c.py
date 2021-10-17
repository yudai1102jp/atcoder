k,n=map(int,input().split())
a=list(map(int,input().split()))


start=a[0]
end=k-a[-1]

m=start+end
for i in range(1,n):
    m=max([m,a[i]-a[i-1]])

print(k-m)