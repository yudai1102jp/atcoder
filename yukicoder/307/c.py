N, K = input().split()
N = int(N)
c_ori = list(map(int, input().split()))
if len(K) > N:
    print(-1)
    exit()
elif len(K) < N:
    print(''.join([''.join([str(j+1) for i in range(c[j])])
          for j in range(9)]))
    exit()
M = []
K_int = int(K)
K_toukei = [0]*9

for i in range(N):
    K_toukei[int(K[i])-1] += 1


def check(s, k):
    for i in range(len(s)):
        if int(s[i]) > int(k[i]):
            return True
    return False


def dfs(s, n, used, flag):
    if n == N:
        return s
    use = [c[i]-used[i] for i in range(9)]
    if flag:

        for i in range(int(K[n]), 10):
            if use[i-1]:
                usedT = list(used)
                usedT[i-1] += 1
                if i != int(K[n]):
                    temp = dfs(s+[i], n+1, usedT, False)
                temp = dfs(s+[i], n+1, usedT, True)

                if check(temp, K):
                    return temp

    return dfs(s, n, used, False)


c = list(c_ori)
ans = []
flag = True
for i in range(N):
    if c[K[i]] and flag:
        c[K[i]] -= 1
        ans.append(K[i])
    else:
        flag = False
        for j in range(9):
            if c[j]:
                ans.append(j)
                c[j] -= 1
                break
if check(ans, K):

    for i in dfs([], 0, [0]*9, True):

        print(i, end='')
    print()
else:
    for i in range(N):
    if c[K[i]] and flag:
        c[K[i]] -= 1
        ans.append(K[i])
    else:
        flag = False
        for j in range(9):
            if c[j]:
                ans.append(j)
                c[j] -= 1
                break
