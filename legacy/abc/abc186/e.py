import math
t=int(input())

def new_func():
    return 1

for i in range(t):
    n,s,k=list(map(int,input().split()))

    k%=n
    Gcd=math.gcd(k,n)
    if ((n-s)%Gcd==0):
        co=new_func()
        while True:
            if ((n*co-s)%k==0):
                x=(n*co-s)//k
                break
            co+=1

        print(x)
    else:
        print(-1)


