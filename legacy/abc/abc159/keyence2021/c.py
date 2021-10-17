

H, W, k = list(map(int, input().split()))

#  R=1    D=2    X=3
a = [[0 for i in range(W)] for j in range(H)]
ans = list(a)

for i in range(k):
    H, W, C = input().split()
    if C == 'R':
        n = 1
    elif C == 'D':
        n = 2
    else:
        n = 3

    a[int(H)-1][int(W)-1] = n
for i in a:
    print(i)


for h in range(H):
    for w in range(W):
        pass
