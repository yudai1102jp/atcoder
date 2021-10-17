s = input()

n=0
su=0
ndic = {1: 0, 2: 0, 0: 0}
for i in s:
    j = int(i)
    n+=1
    su+=j
    ndic[j % 3] += 1



if su%3==0:
    print(0)
elif (su%3==1):
    if ndic[1]:
        if n==1:
            print(-1)
        else:
            print(1)
    else:
        if n==2:
            print(-1)
        else:
            print(2)
elif su%3==2:
    if ndic[2]:
        if n==1:
            print(-1)
        else:
            print(1)
    else:
        if n==2:
            print(-1)
        else:
            print(2)