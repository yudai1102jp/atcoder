
N, M = list(map(int, input().split()))
B = [[int(i) for i in input().split()] for j in range(N)]

now = [(B[0][0]-1)//7, (B[0][0]-1) % 7]

for i in range(N):
    for j in range(M):
        if j+now[1] <= 6 and B[i][j] == (now[0]+i)*7+(now[1]+j+1):
            continue
        print('No')
        exit()
print('Yes')
