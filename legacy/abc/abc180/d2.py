
x, y, a, b = map(int, input().split())
count = 0
while x*(a-1) < b and y>x*a:
    
    x *= a
    count += 1


temp = (y-x-1)//b


count += int(temp)

print(count)
