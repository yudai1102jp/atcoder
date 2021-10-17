n=int(input())


li=[abs(int(i)) for i in input().split()]

m=0
u2=0
t=0

for i in li:
    m+=i
    u2+=i*i
    t=max(t,i)

print(m)
print(pow(u2,1/2))
print(t)
