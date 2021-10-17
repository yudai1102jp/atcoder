# a = list(input())
S = list(input())
# A=[[int(i) for i in input().split()] for j in range(N)]

min = S[:]
max = S[:]
now = 0
for i in range(1, len(S)):
    temp = S[i:]+S[:i]
    if temp > max:
        max = temp[:]
    if temp < min:
        min = temp[:]
print(''.join(min))
print(''.join(max))
