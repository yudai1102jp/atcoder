n = int(input())

if 1000 > n:
    print(0)
else:
    ans=0
    for i in range(1,7):
        if n>=10**(i*3):
            ans += n-10**(i*3)+1
    print(ans)