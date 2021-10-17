N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

score = 0
temp = A[0]+1
for i in A:
    if temp-1 != i:
        score += temp
    temp = i


print(score+A[-1])
