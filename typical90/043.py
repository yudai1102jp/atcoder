
from collections import deque


def convertxy(allow):
    if allow == 0:
        return 1, 0
    elif allow == 1:
        return 0, 1
    elif allow == 2:
        return -1, 0
    elif allow == 3:
        return 0, -1


H, W = map(int, input().split())

rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

S = [input() for i in range(H)]
MAP = [[[] for i in range(W)] for j in range(H)]

Check = [[[1000*1000+76, 1000*1000+76, 1000*1000+76, 1000*1000+76]
          for i in range(W)] for j in range(H)]

q = [deque()]*(1000*1000+2)
q[0].append((rs-1, cs-1))
MAP[rs-1][cs-1] = [0, set([0, 1, 2, 3])]


rt -= 1
ct -= 1
now = 0
while True:
    if not q[now]:
        now += 1

    r, c = q[now].popleft()
    co, allow = MAP[r][c]
    if Check[r][c]:
        continue
    Check[r][c] = True

    if r == rt and c == ct:

        break
    for i in range(4):
        x, y = convertxy(i)
        ner = r+x
        nec = c+y
        if not (0 <= nec < W and 0 <= ner < H and S[ner][nec] == '.'):
            continue

        if i in allow:
            if (not (MAP[ner][nec])) or MAP[ner][nec][0] > co:
                MAP[ner][nec] = [co, set([i])]
                q[co].append((ner, nec))
            elif MAP[ner][nec][0] == co:
                MAP[ner][nec][1].add(i)
        else:
            if (not (MAP[ner][nec])) or MAP[ner][nec][0] > co+1:
                MAP[ner][nec] = [co+1, set([i])]
                q[co+1].append((ner, nec))
            elif MAP[ner][nec][0] == co+1:
                MAP[ner][nec][1].add(i)


print(MAP[rt][ct][0])
