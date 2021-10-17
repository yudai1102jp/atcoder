N, K = map(int, input().split())
AB = [[int(i) for i in input().split()] for j in range(N)]

tokuten = []

ans = 0
for i in range(N):
    tokuten.append(AB[i][1])
    tokuten.append(AB[i][0]-AB[i][1])
tokuten.sort(reverse=True)

print(sum(tokuten[:K]))
