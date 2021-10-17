# a=map(int, input().split())

s = list(input())
t = list(input())

f = 0
flag = False
for i in range(len(s)-1):
    if s[i] != t[i]:
        s[i+1], s[i] = s[i], s[i+1]

        break
for i in range(len(s)):
    if s[i] != t[i]:
        print('No')

        break
else:
    print('Yes')
