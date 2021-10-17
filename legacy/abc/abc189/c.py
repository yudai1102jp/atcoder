n=int(input())
a=[int(i) for i in input().split()]


ans=0


s=-1
e=-1
Min=0
for l in range(n):
    if (Min<a[l]):
        Min = a[l]
        for r in range(l, n):
            Min=min([Min, a[r]])
            
            
            temp=Min*(r-l+1)

            if temp>ans:

                ans=temp
                s=l
                e=r
print(ans)