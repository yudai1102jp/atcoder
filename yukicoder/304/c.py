N = int(input())
HW = [[int(i) for i in input().split()] for j in range(N)]

li = [0]*(2**5+4)
ans = 0
for i in range(N):
    if HW[i][0] == HW[i][1]:
        continue
    li[HW[i][1]] += 1
tan = 0
for i in range(N):

    if li[HW[i][0]]:

        ans += li[HW[i][0]]
    else:
        tan += 1
if tan > 2:
    print(0)
else:
    print(ans)
