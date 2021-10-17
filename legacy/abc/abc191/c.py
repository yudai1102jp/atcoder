H, W = map(int, input().split())
s = [input() for j in range(H)]


def reverse(x, y):
    if x == -1:
        x = 1
    elif x == 1:
        x = -1
    if y == -1:
        y = 1
    elif y == 1:
        y = -1
    return x, y


ans = 0
for h in range(H-1):
    for w in range(W-1):
        bk = 0
        for dx, dy in [(1, 0), [1, 1], [0, 1], [0, 0]]:
            if s[h+dx][w+dy] == '#':
                bk += 1
        if bk % 2:
            ans += 1
print(ans)
