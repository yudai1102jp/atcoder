
import copy

N=int(input())





if N%2==0:
    for i in range(2**N):
        co=0
        li=[0]*N
        for j in range(N):
            if i&1<<(N-j-1):
                co-=1
                if co<0:
                    break
                li[j]=0
                
            else:

                co+=1
                li[j]=1
        else:
            if co==0:
                print(''.join(['(' if j else ')' for j in li]))
        
    
    
else:
    print('')

    
