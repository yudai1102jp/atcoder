n, m = map(int, input().split())
AB = [[int(i) for i in input().split()] for j in range(m)]
k = int(input())
CD = [[int(i) for i in input().split()] for j in range(k)]


ans = 0
A = {i: 0 for i in range(1, n+1)}
for i in range(k):
    A[CD[i][0]] += 1
for i in range(m):
    if A[AB[i][0]] and A[AB[i][1]]:
        ans += 1


for i in range(1, pow(2, n)):
    now = (i-1) ^ i

    for j in range(k):

        if (now >> j) & 1:

            if ((i >> j) & 1):

                A[CD[j][1]] += 1
                A[CD[j][0]] -= 1
            else:
                A[CD[j][1]] -= 1
                A[CD[j][0]] += 1

    count = 0
    for j in range(m):
        if A[AB[j][0]] and A[AB[j][1]]:
            count += 1
    ans = max([ans, count])
print(ans)
