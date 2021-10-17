b,c=map(int,input().split())
ans=0
# 0 direct
if b==0:
    print(c)
elif b<0 and abs(b)*2<c:
    ans+=abs(b)*2+1
    ans+=c-1
    print(ans)
elif b>0 and b*2<=c:
    ans+=b*2+1
    ans+=c-2
    print(ans)
else:
    if c>2 and c%2==1:
        print(c*2-1)
    elif c==1:
        print(c+1)
    elif c==2:
        print(c+1)
    elif c%2==0:
        print(2*c-1)
    
