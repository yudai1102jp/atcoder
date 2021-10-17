x = input()
n = int(input())
s = [input() for s in range(n)]

a_x = {chr(ord('a')+i): x[i] for i in range(ord('z')+1-ord('a'))}
x_a = {x[i]: chr(ord('a')+i) for i in range(ord('z')+1-ord('a'))}
new_s = []
for i in s:
    temp = []
    for j in i:
        temp.append(x_a[j])
    new_s.append(''.join(temp))

new_s.sort()

for i in new_s:
    ans = []
    for j in i:
        ans.append(a_x[j])
    print(''.join(ans))
