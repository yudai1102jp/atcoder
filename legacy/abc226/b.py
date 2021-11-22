
N = int(input())
La = [[int(i) for i in input().split()] for j in range(N)]

# print(len(set(La)))
La.sort()
# La.sort()
ans = 1
for i in range(1, N):
    for j in range(La[i][0]+1):
        if La[i-1][j] != La[i][j]:
            ans += 1
            break
print(ans)
