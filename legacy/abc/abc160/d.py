n, x, y = map(int, input().split())


s = {i: 0 for i in range(1, n+1)}
for i in range(1, n):
    for j in range(i+1, n+1):
        co = min([j-i, abs(i-x)+1+abs(j-y), abs(i-y)+1+abs(j-y)])
        s[co] += 1
for i in range(1,n):
    print(s[i])
