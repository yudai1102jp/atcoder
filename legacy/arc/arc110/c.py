n=int(input())
p=list(map(int,input().split()))


ans=[]
flag=True
ope=[]
for i in range(1,n+1):
    index=p.index(i) +1
    if index!=i:
        for j in range(index,i,-1):
            temp1=p[j-1]
            temp2=p[j-2]
            p[j-1]=temp2
            p[j-2]=temp1
      
            ans.append(j-1)
        for j in ans:
            if p[j-1]!=j:
                print(-1)
                flag=False
        

for i in range(1,n):
    if i not in ans:
        print(-1)
        flag(False)
if flag:
    for i in ans:
        print(i)