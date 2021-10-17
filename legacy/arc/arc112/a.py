t=int(input())
Case=[[int(_) for _ in input().split()] for i in range(t)]

for l,r in Case:
    if l*2<=r:
        n=r-2*l+1
        print((n)*(1+n)//2)


    else:
        print(0) 