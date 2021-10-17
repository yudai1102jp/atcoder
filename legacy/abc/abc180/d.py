import math


x,y,a,b=map(int,input().split())


count=int(math.log(int(b/x),a))


temp=(y-x*count)/b
if temp-int(temp)==0:
    count += int((y-x*count)/b)-1
else:
    count += int((y-x*count)/b)
    
print(count)
