n, m = map(int, input().split())

a = list(map(int, input().split()))


Sum = sum(a)/(4*m)
co = 0
for i in a:
    if i >= Sum:
        co += 1

if co >= m:
    print('Yes')
else:
    print('No')
