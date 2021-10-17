K = int(input())

A, B = input().split()

a = 0
b = 0
for i in range(len(A)):
    a += int(A[len(A)-1-i])*pow(K, i)
for i in range(len(B)):
    b += int(B[len(B)-1-i])*pow(K, i)

print(a*b)
