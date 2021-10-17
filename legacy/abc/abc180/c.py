from collections import deque

n=int(input())

sqrt=int(pow(n,1/2))

d=deque()
if sqrt**2==n:
    d.appendleft(sqrt)
    sqrt-=1
for i in range(sqrt,0,-1):
    if n%i==0:
        d.appendleft(i)
        d.append(int(n/i))


for i in d:
    print(i)