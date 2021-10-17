s=input()
n=1
flag=False
for i in s:

    if i.islower() and n%2==0:
        flag=True
    elif n%2==1 and not i.islower():
        
        flag=True
    n+=1
if flag:
    print('No')
else:
    print('Yes')
