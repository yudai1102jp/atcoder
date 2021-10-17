
num = input()
x = [int(i) for i in num]


x.reverse()
m = int(input())


ma = max([int(i) for i in x])



Min = ma
Max = pow(10,18)+3
n = Min+1

if len(x) == 1:
    if x[0] <= m:
        print(1)
    else:
        print(0)


else:
    while True:
        now = 0
        for i in range(len(x)):
            now += x[i]*pow(n, i)

        if m >= now:
            Min = n

        else:
            Max = n
        if Max-Min == 1:
            break
        n = Min+(Max-Min)//2
    print(Min-ma)
