n=int(input())

x=[]
y=[]

for i in range(n):
    _x, _y =map(int,input().split())
    x.append(_x)
    y.append(_y)



def check(x , y):
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                x1=x[i]
                y1=y[i]
                x2=x[j]
                y2=y[j]
                x3=x[k]
                y3=y[k]

                x1-=x2
                y1-=y2
                x3-=x2
                y3-=y2

                if y1*x3==y3*x1:
                    return True
                
    return False


if check(x,y):
    print('Yes')
else:
    print('No')

