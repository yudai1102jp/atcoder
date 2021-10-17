n=int(input())
ans=0


for i in range(1,n+1):
    check_10=int(i)
    check_8=int(i)
    bool=True
    while check_10>6:
        if check_10%10==7:
            ans+=1
            bool=False
            break
        check_10//=10
    while bool and check_8>6:
        if check_8%8==7:
            ans+=1
            break
        check_8//=8



print(n-ans)