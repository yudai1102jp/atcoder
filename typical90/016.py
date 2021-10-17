N = int(input())

A, B, C = list(map(int, input().split()))


ans = 10000

for i in range(10000):
    if A*i > N or ans <= i:
        break
    for j in range(10000):
        if i+j > 10000 or A*i + B*j > N or ans <= i+j:
            break
        if (N-A*i-B*j) % C == 0:
            now = i+j+((N-A*i-B*j) // C)
            ans = min(ans, now)
print(ans)
