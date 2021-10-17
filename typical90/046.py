N = int(input())
A = list(map(lambda x:  int(x) % 46, input().split()))
B = list(map(lambda x:  int(x) % 46, input().split()))
C = list(map(lambda x:  int(x) % 46, input().split()))


A_dict = [0]*46
B_dict = [0]*46
C_dict = [0]*46

for i in range(N):
    A_dict[A[i]] += 1
    B_dict[B[i]] += 1
    C_dict[C[i]] += 1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 == 0:
                ans += A_dict[i]*B_dict[j]*C_dict[k]
print(ans)
