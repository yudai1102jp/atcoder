n, k, c = map(int, input().split())
s = input()

co = 0
now = 0
f = []
l = []
while co < k:
    if s[now] == 'o':
        co += 1
        f.append(now+1)
        now += c+1

    else:
        now += 1
    if now>=n:
        break
now = n-1
co = 0
while co < k:
    if s[now] == 'o':
        co += 1
        l.append(now+1)
        now -= c+1
    else:
        now -= 1
    if now<0:
        break
l.sort()
ans=[]
for i in range(min([len(f), len(l)])):
    if f[i]==l[i]:
        ans.append(f[i])



if ans:
    ans.sort()
for i in ans:
    print(i)
