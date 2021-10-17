n,x=map(int,input().split())

a=[int(i) for i in input().split()]


for i in range(n):
    if a[i]!=x:
    
        if i!=n-1:
            print(a[i], end=' ')
        else:
            print(a[i], end='')
print()

    