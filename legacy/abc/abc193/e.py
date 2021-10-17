
import math
t = int(input())


xypq = [[int(i) for i in input().split()] for _ in range(t)]

for x, y, p, q in xypq:

    Tt = (x+y)*2
    Th = (p+q) 
    t = x
    lcm = Tt*Th/math.gcd(Tt, Th)
    count = 1
    while t < lcm:
        if p - (t % Th) < y:
            a = p - (t % Th)
            if a:
                print(t+a)
            else:
                print(t)
            break

        t += Tt
        count += 1
    else:
        print('infinity')
        
