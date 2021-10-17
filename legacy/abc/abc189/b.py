n,x=map(int,input().split())
x*=100
now=0
for i in range(n):
    a,b=map(int,input().split())
   
    now+=a*b
    if x<now:
        print(i+1)
        break
else:
    print(-1)
