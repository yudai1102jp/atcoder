h, w = map(int, input().split())

A = [[int(i) for i in input().split()] for j in range(h)]
R_sum = [sum(i) for i in A]
C_sum = [0]*w
for i in range(w):
    C_sum[i] = sum([r[i] for r in A])

for i in range(h):
    print(' '.join(map(str, [R_sum[i]+C_sum[j]-A[i][j] for j in range(w)])))
