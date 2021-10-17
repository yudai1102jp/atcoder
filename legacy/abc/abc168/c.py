import math


a,b,h,m=map(int,input().split())

h_theta=(h+m/60)*math.pi/6


m_theta=m*math.pi/30

theta=abs(h_theta-m_theta)

if theta>math.pi:
    theta=2*math.pi-theta
print(math.sqrt(a**2+b**2-2*a*b*math.cos(theta)))