import math


n = int(input())
ans = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        ab=math.gcd(a,b)
        if ab==1:
            ans+=n
        else:
            for c in range(1, n+1):
                ans += math.gcd(ab, c)
print(ans)
