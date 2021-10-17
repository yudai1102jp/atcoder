n, s, d = map(int, input().split())
xy = [[int(i) for i in input().split()] for j in range(n)]


flag = True
for i in range(n):
    x, y = xy[i]
    if x < s and y > d:
        print('Yes')
        break
else:
    print('No')
