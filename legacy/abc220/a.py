A, B, C = map(int, input().split())

for i in range(0, B+1, C):
    if i >= A:
        print(i)
        break
else:
    print(-1)
