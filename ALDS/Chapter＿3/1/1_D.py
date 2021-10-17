n=int(input())

r=[]
min=10000000000
Max=0
ans=-1
for i in range(n):
    temp=int(input())
    if min >temp:
        ans=max([ans,Max-min])
        min=temp
        Max=0
    else:
        Max=max([Max,temp])
    


print(max([ans,Max-min]))

