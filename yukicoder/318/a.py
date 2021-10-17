T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    if not(A[0] == 1 and A[-1] == N):
        print('No')
        continue

    flag = False
    chs = 0
    che = 0
    count = {i+1: 0 for i in range(N)}
    for i in range(2*N):
        count[A[i]] += 1
        if A[i] != i % N+1 and not flag:

            chs = i-1
            flag = True
            continue
        if flag and A[i] == A[chs]:
            che = i
    for i in range(N):
        if count[i+1] != 2:
            print('No')
            break
    else:
        for i in range(2*N):
            if chs < i < che:
                i_ = che-(i-chs)
            else:
                i_ = i
            if A[i_] != i % N+1:
                print('No')
                break
        else:
            print('Yes')
