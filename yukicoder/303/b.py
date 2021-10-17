N = int(input())
A = list(map(int, input().split()))

S = sum(A)
if S % N == 0:
    print('Yes')
else:
    print('No')
# for i in A[1:]:
#     if flag == i % 2:
#         continue
#     print('No')
#     exit()
# print('Yes')
