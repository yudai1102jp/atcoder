
h,w,k=map(int,input().split())

li=[[int(i) for i in input().split()] for j in range(h)]
ans=int("inf")

# for i in range(2**(h-1)):   
#     if 
#     li_sum1=

    
    
    
temp_li=list(li)
for j in range(h):

    temp_li+=li[i]
temp=0
for j in range(w):
    temp+=temp_li[j]
    if temp>k:
        temp=0
        count+=1

ans=max(count,ans)

print(ans)