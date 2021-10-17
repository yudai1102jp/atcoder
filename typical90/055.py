N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i1 in range(N-4):
    for i2 in range(i1+1, N-3):
        temp1 = A[i1]*A[i2] % P
        for i3 in range(i2+1, N-2):
            temp2 = temp1*A[i3] % P
            for i4 in range(i3+1, N-1):
                temp3 = temp2*A[i4] % P
                for i5 in range(i4+1, N):
                    if temp3*A[i5] % P == Q:
                        ans += 1
print(ans)
