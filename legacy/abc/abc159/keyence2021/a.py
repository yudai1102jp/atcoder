n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ans = []
anum = 0
amax = 0
bnum = 0

abnum = 0
for i in range(n):
    amax=max([amax,a[i]])
    
    # if bnum <= b[i] :
    #     bnum = b[i]
    #     anum=amax


    #     abnum = anum*bnum


   

    if abnum<amax*b[i]:
        anum=amax
        bnum=b[i]
        abnum=anum*bnum
        
    ans.append(abnum)

for i in ans:

    print(i)
