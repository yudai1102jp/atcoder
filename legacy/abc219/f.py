s = input()
k = int(input())
count = {'U': 0, 'D': 0, 'R': 0, 'L': 0}
for i in s:
    count[i] += 1
h = abs(count['U']+count['D'])
w = abs(count['R']+count['L'])

floor = [[False for i in range(w)] for j in range(h)]
now = [count['U'], count['L']]
floor[now[0]][now[1]] = True
for i in range(len(s)):
    if s[i] == 'U':
        now[0] -= 1
    elif s[i] == 'D':
        now[0] += 1
    elif s[i] == 'R':
        now[1] += 1
    elif s[i] == 'L':
        now[1] -= 1
    floor[now[0]][now[1]] = True

move = [now[0]-count['U'], now[1]-count['L']]


sh = -1
eh = -1
sw = -1
ew = -1

for y in range(h):
    for x in range(w):
        if sh == -1 and floor[y][x]:
            sh = y

        if sw == -1 and floor[x][y]:
            sw = y
        if eh == -1 and floor[h-1-y][x]:
            eh = h-1-y
        if ew == -1 and floor[x][w-1-y]:
            sw = w-1-y
    if sh != -1 and sw != -1 and eh != -1 and ew != -1:
        break

juuhuku = [(eh-sh)//move[0]-1, (ew-sw)//move[1]-1]
juuhuku_list = [0]*juuhuku

for h in range(sh, sh+1+move[0]):
    for w in range(sw, ew+1):
        flag_non = True
        juu = 0
        while juu <= juuhuku[0] and (h+juu*move[0] < eh+1 and w+juu*move[1] < ew+1):
            if flag_non and floor[h+juu*move[0]][w+juu*move[1]]:
                flag_non = False
            else:
                juuhuku_list[juu] += 1
            juu += 1


for w in range(sw, sw+1+move[1]):
    for h in range(move[0], ew+1):
        flag_non = True
        juu = 0
        while juu <= juuhuku[0] and (h+juu*move[0] < eh+1 and w+juu*move[1] < ew+1):
            if flag_non and floor[h+juu*move[0]][w+juu*move[1]]:
                flag_non = False
            else:
                juuhuku_list[juu] += 1
            juu += 1

ans =
