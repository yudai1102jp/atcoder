N = int(input())
A = list(map(int, input().split()))
print('+-'+'--'*N)
for h in range(max(A)):
    print('|.', end='')
    for n in range(N):
        s = 'X.' if A[n] > 1 else 'V.' if A[n] == 1 else '..'
        A[n] -= 1
        print(s, end='')

    print()


print('+-'+'--'*N)
