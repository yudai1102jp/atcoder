import sys  # 追加
sys.setrecursionlimit(500*500)

N = 2**20


def init_min(init_min_val):
    # set_val
    for i in range(N):
        seg_min[i+num_min-1] = init_min_val[i]
    # built
    for i in range(num_min-2, -1, -1):
        seg_min[i] = min(seg_min[2*i+1], seg_min[2*i+2])


def update_min(k, x):
    k += num_min-1
    seg_min[k] = x
    while k:
        k = (k-1)//2
        seg_min[k] = min(seg_min[k*2+1], seg_min[k*2+2])


def query_min(p, q):
    if q <= p:
        return ide_ele_min
    p += num_min-1
    q += num_min-2
    res = ide_ele_min
    while q-p > 1:
        if p & 1 == 0:
            res = min(res, seg_min[p])
        if q & 1 == 1:
            res = min(res, seg_min[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res, seg_min[p])
    else:
        res = min(min(res, seg_min[p]), seg_min[q])
    return res


A = [-1]*(N)
Q = int(input())
tx = [[int(i) for i in input().split()] for j in range(Q)]

#####単位元######
ide_ele_min = 10**18+5

# num_min:n以上の最小の2のべき乗
num_min = 2**(N-1).bit_length()
seg_min = [ide_ele_min]*2*num_min
init_min(A)


for t, x in tx:
    if t == 1:
        ok = (x-1) % N
        ng = N
        if query_min(ok, ng) >= 0:

            ng = ok
            ok = 0
        while ng-ok != 1:
            now = (ng+ok)//2
            a = query_min(ok, now)
            if a == -1:
                ng = now
            else:
                ok = now

        update_min(ok, x)

        # while A[x % N] != -1:
        #     x += 1
        # A[x % N] = x
    else:
        print(query_min((x-1) % N, (x-1) % N+1))
