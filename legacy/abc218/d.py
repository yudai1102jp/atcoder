N = int(input())


xs = []
ys = []
for i in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xdict = {x: i for i, x in enumerate(sorted(list(set(xs))))}
ydict = {y: i for i, y in enumerate(sorted(list(set(ys))))}

map = [[False for i in range(len(ydict))] for j in range(len(xdict))]


for i in range(N):
    map[xdict[xs[i]]][ydict[ys[i]]] = True

ans = 0
for iy in range(len(xdict)-1):
    for ix in range(len(ydict)-1):
        if not map[iy][ix]:
            continue
        for jy in range(iy+1, len(xdict)):
            if not map[jy][ix]:
                continue
            for jx in range(ix+1, len(ydict)):
                if map[iy][jx] and map[jy][jx]:
                    ans += 1

print(ans)
