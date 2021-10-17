n=int(input())
s=[]
boo=[1,1]
for i in range(n):
    if (input()=='OR'):
        boo = [boo[0], boo[0]+boo[1]*2]
    else:
        boo=[boo[0]*2+boo[1],boo[1]]
        

print(boo[1])
