n, m, q = map(int, input().split())

wv = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    wv[i] = [wv[i][1], wv[i][0]]
wv.sort(reverse=True)
for i in range(n):
    wv[i] = [wv[i][1], wv[i][0]]


x = list(map(int, input().split()))

for i in range(q):
    L, R = map(int, input().split())
    ans = 0
    used_box = set()
    temp_x = []
    if L != 1:
        temp_x += (x[0:L-1])
    if R != m:
        temp_x += (x[R: m])
    if L == 1 and R == m:
        print(0)
    else:
        for WV_n in wv:
            value = 0
            temp_x_n = -1
            for j in range(len(temp_x)):
                if WV_n[0] <= temp_x[j] and (j not in used_box):

                    if temp_x_n == -1 or temp_x[temp_x_n] > temp_x[j]:
                        temp_x_n = j
            used_box.add(temp_x_n)
            if temp_x_n != -1:
                ans += WV_n[1]
        print(ans)
