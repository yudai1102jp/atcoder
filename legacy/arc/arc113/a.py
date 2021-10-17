k=int(input())
a=1



ans=0
while True:
    
    b=a
    if a > k//(a*b):
        break
    while True:
        
        c_co = k//(a*b)
        if b <=c_co:
                
            if a==b:
                ans+=1+(c_co-b)*3
            else:
                ans+=3+(c_co-b)*6
                
        else:
            break
        b+=1
    a+=1

print(ans)
