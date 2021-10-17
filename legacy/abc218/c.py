N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


character = []
new = []

start_tate = -1
start_yoko = -1
end_tate = -1
end_yoko = -1
for i in range(N):
    if '#' in S[i] and start_tate == -1:
        start_tate = i
    if '#' in S[i]:
        end_tate = i
    for j in range(N):
        if S[i][j] == '#' and start_yoko == -1:
            start_yoko = j
        if S[i][j] == '#':
            start_yoko = min(start_yoko, j)
            end_yoko = max(end_yoko, j)
new_S = [i[start_yoko:end_yoko+1] for i in S[start_tate:end_tate+1]]
Syoko = end_yoko-start_yoko+1
State = end_tate-start_tate+1


Tstart_tate = -1
Tstart_yoko = -1
Tend_tate = -1
Tend_yoko = -1
for i in range(N):
    if '#' in T[i] and Tstart_tate == -1:
        Tstart_tate = i
    if '#' in T[i]:
        Tend_tate = i
    for j in range(N):
        if T[i][j] == '#' and Tstart_yoko == -1:
            Tstart_yoko = j
        if T[i][j] == '#':
            Tstart_yoko = min(Tstart_yoko, j)

            Tend_yoko = max(Tend_yoko, j)
new_T = [i[Tstart_yoko:Tend_yoko+1] for i in T[Tstart_tate:Tend_tate+1]]


yoko = Tend_yoko-Tstart_yoko+1
tate = Tend_tate-Tstart_tate+1
new__T = [['' for i in range(tate)] for j in range(yoko)]
flag = True


for i in range(tate):
    for j in range(yoko):
        new__T[yoko-j-1][i] = new_T[i][j]
        if State != tate or Syoko != yoko or new_S[i][j] != new_T[i][j]:
            flag = False
if flag:
    print('Yes')
    exit()

new_T = new__T[::]

new__T = [['' for i in range(yoko)] for j in range(tate)]
flag = True
for i in range(yoko):
    for j in range(tate):
        new__T[tate-j-1][i] = new_T[i][j]

        if State != yoko or Syoko != tate or new_S[i][j] != new_T[i][j]:

            flag = False
if flag:
    print('Yes')
    exit()
new_T = new__T[::]
new__T = [['' for i in range(tate)] for j in range(yoko)]
flag = True
for i in range(tate):
    for j in range(yoko):
        new__T[yoko-j-1][i] = new_T[i][j]

        if State != tate or Syoko != yoko or new_S[i][j] != new_T[i][j]:

            flag = False
if flag:
    print('Yes')
    exit()

new_T = new__T[::]
flag = True
for i in range(yoko):
    for j in range(tate):
        if State != yoko or Syoko != tate or new_S[i][j] != new_T[i][j]:

            flag = False
if flag:
    print('Yes')
    exit()
print('No')
