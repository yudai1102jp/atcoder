n=int(input())
A=list(map(int,input().split()))

A.sort(reverse=True)



ans=0
dp=[]

for i in range(n-1):
    ans+=A[0]-A[i+1]

dp.append(ans)
for i in range(1,n-1):
    ans+=dp[-1]-(A[i-1]-A[i])*(n-i)
    dp.append(dp[-1]-(A[i-1]-A[i])*(n-i))
print(ans)