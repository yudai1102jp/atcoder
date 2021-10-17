import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())


for i in range(Q):
    e = int(input()) % T

    nowy = -math.sin(e*2*math.pi/T)*L/2
    nowz = -(math.cos(e*2*math.pi/T)-1) * L/2
    dict = math.sqrt(X**2+(Y-nowy)**2)
    print(math.atan(nowz/dict)*180/(math.pi))
