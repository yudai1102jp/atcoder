N = int(input())
c = list(map(int, input().split()))
for i in range(1, 10):
    for j in range(c[-i]):
        print(10-i, end='')


print()
