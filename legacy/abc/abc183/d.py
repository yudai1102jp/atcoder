n, w = map(int, input().split())
stp = [list(map(int, input().split())) for i in range(n)]

t = [0 for i in range(200005)]

for i in stp:
    t[i[0]] +=i[2]
    t[i[1]] -=i[2]
    
ma=0
now=0
for i in t:
    now+=i
    ma=max(ma,now)

if ma > w:
    print('No')
else:
    print('Yes')
