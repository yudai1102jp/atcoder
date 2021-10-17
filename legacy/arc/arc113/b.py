a,b,c=map(int,input().split())
g=a%10
if g==0 or g==1:
    print(g)
else:
    p=1
    temp=a%10
    cal=pow(temp,2,10)

    while temp !=cal:
        cal*=temp
        cal%=10
        p+=1


    po=pow(b,c,p)
    if po==0:
        po=p

    print(pow(a,po,10))