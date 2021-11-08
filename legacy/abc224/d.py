from collections import deque

# a = list(input())
M = int(input())
uv = [[int(i) for i in input().split()] for j in range(M)]
p = list(map(int, input().split()))
for i in range(8):
    p[i] -= 1

load={}


class passed:
    def __init__(self, co=0) -> None:
        self.node = [0 for i in range(9)]
        if co < 8:
            for i in range(9):
                self.node[i] = passed(co+1)

    def check(self, p):
        now_node = self.node
        flag = True
        for i in range(7):
            if flag and p[i] != i:
                flag = False
            now_node = self.node[p[i]]
        if flag and p[-1] == 7:
            return 2
        if now_node[7] == 0:
            now_node[7] = 1
            return 0
        else:
            return 1


load = [[] for i in range(9)]
for i in range(M):
    load[uv[i][0]-1].append(uv[i][1]-1)
    load[uv[i][1]-1].append(uv[i][0]-1)


q = deque()

empty = 36
for i in p:
    empty -= i
q.append((p[:], empty, 0))
ans = -1
passed = passed(0)
while q:
    now, empty, co = q.popleft()
    ch = passed.check(now)
    if ch == 1:
        continue
    elif ch == 2:
        ans = co
        break

    for ne in load[empty]:
        next = now[:]
        for i in range(8):
            if next[i] == ne:
                next[i] = empty
                break
        q.append((next, ne, co+1))


print(ans)
