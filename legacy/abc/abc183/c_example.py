import itertools

n, k = map(int, input().split())

t = [list(map(int, input().split())) for i in range(n)]


ans = 0
co = 0
for i in itertools.permutations(range(2, n+1)):
    co = 0
    li = [1]+list(i)+[1]
    for j in range(n):
        co += t[li[j]-1][li[j+1]-1]
    ans += 1 if co == k else 0

print(ans)
