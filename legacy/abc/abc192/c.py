from functools import reduce
s,k=input().split()
n=[]
for i in s:
    n.append(int(i))


k=int(k)

for i in range(k):
    g2=sorted(n)
    g1=g2[::-1]
    temp = reduce(lambda a, b: 10*a+b, g1) -  reduce(lambda a, b: 10*a+b, g2)
    n=[int(c) for c in str(temp)]
print(reduce(lambda a, b: 10*a+b, n))
