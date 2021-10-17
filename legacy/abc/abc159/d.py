from collections import Counter
import math

n=int(input())

n=[int(i) for i in input().split()]

co=Counter(n)

summ={}
for k, v in co.items():
    summ[k]=(v-1)*v//2


anssum=0
for v in summ.values():
    anssum+=v





for i in n: 
    tar=co[i]
    print(anssum-tar+1)