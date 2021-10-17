n,k=map(int,input().split())

x=n%k

x=min([x,abs(x-k)])

print(x)