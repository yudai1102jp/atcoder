import collections
N = int(input())


# for B_ in B:
#     no.append(B_)
# for B_ in A:
#     no.append(B_)
Ans = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if(i+j > N-1):
            Ans[i][j] = 2
        elif(i+j == N-1):
            if(i <= j):
                Ans[i][j] = 1
            else:
                Ans[i][j] = 2
for i in range(N):
    print(*Ans[i], sep="")
