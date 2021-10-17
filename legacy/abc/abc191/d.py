import math
X, Y, R = [round(10000*float(i)) for i in input().split()]
r = pow(R, 2)


ans = 0
for i in range(round((X-R), -4)-10000, round((X+R),-4)+30000, 10000):
    yp2 = r-pow(i-X, 2)
    if yp2>=0:
        
        ym = yp*-1
        yp += Y
        if int(ym) == ym:
            ans += 1
        ans += int(yp)-int(ym)
print(ans)
