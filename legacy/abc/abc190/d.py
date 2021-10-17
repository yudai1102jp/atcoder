
import math
n = int(input())


ans = 1
s = 2*n

for i in range(2, 1+int(math.sqrt(s))):
    if s % i == 0:
        if (s/i-i+1) % 2 == 0:
            ans += 1


print(2*ans)
