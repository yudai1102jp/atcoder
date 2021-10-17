N = int(input())


cp1 = [0]*(N+1)
cp2 = [0]*(N+1)

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        cp1[i+1] = cp1[i]+p
        cp2[i+1] = cp2[i]

    else:
        cp2[i+1] = cp2[i]+p
        cp1[i+1] = cp1[i]

for i in range(int(input())):
    l, r = map(int, input().split())
    l -= 1
    print(f'{cp1[r]-cp1[l]} {cp2[r]-cp2[l]}')
