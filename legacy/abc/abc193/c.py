import math

n = int(input())



if n <= 3:
    print(n)

else:


    ans=0
    se=set()
    for i in range(2,n):
        if i in se:
            continue

        

   
        temp=math.log(n,i)

        if temp>=2:
            ans += int(temp)-1
            se|={i**j for j in range(2,int(temp)+1)}
        else:
            break
    print(n-ans)
