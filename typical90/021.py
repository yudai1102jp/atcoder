N, M = map(int, input().split())
allow = [set() for i in range(N)]
non_check = set()
for i in range(M):
    a, b = map(int, input().split())
    allow[a-1].add(b-1)
    non_check.add(a-1)


loop = [set()]
check = set()
temp = set()
ans = 0

check = set()
# for i in range(N):
#     while allow[i]:
#         now = allow[i].pop()
#         if i in allow[now]:
#             ans += 1
# allow[now].rempve(i)
# print(ans)

# for a in allow[now]:
#     if now in allow[a]:
#         ans+=1
#         allow[now].pop(a)
#         allow[a].pop(now)
#     else:
#         allow[now]


def Loop(start, now_check):

    for next in allow[start]:
        if next == goal:
            global loop
            loop[loop_n] = loop[loop_n] | now_check | set([start])
            continue
        if next in now_check:
            global temp
            temp.add(start)
            continue
        if next not in non_check:
            continue
        Loop(next, now_check | set([start]))


goal = 0
loop_n = 0
while non_check:
    t = non_check.pop()
    temp.add(t)
    non_check.add(t)

    while temp:
        goal = temp.pop()
        Loop(goal, set([goal]))
    non_check = non_check-loop[loop_n]-set([t])
    goal += 1
    loop_n += 1
    loop.append(set())

ans = 0
for i in loop:
    ans += len(i)*(len(i)-1)//2
print(ans)
