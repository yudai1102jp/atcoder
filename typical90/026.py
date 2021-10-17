from collections import deque

N = int(input())

tree = [[] for i in range(N)]
tree1 = {i: set() for i in range(N)}

for i in range(N-1):
    a, b = map(int, input().split())

    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    tree1[a-1].add(b-1)
    tree1[b-1].add(a-1)
# tree1 = sorted(tree.items(), key=lambda x: (len(x[1]), x[0]))


tree1 = sorted(tree1.items(), key=lambda x: len(x[1]))

used = set()
ans = [0]*(N//2)
now = 0
for i in range(N):
    if now == N//2:
        break
    if tree1[i][1].isdisjoint(used):
        ans[now] = tree1[i][0]+1
        used.add(tree1[i][0])
        now += 1
num = N//2
if now != num:

    used = set()
    ans = [0]*num
    now = 0
    for i in range(N):
        if now == num:
            break
        if len(tree[i]) == 1:
            ans[now] = i+1
            used.add(i)
            now += 1

    if (now != num):
        q = set([tree[i][0] for i in used])
        used = used | q

        while now < num:
            close = q.pop()
            for next in tree[close]:
                if next in used or now == num:
                    continue
                ans[now] = next+1
                used.add(next)
                now += 1
                if len(tree[next]) > 2:
                    continue
                for j in tree[next]:
                    used.add(j)
                    q.add(j)

while (now != N//2):
    pass
print(' '.join(map(str, ans[:num])))
