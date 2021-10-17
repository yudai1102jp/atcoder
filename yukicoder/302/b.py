a, b = sorted(list(map(int, input().split())))

if a % 2 == 1 and b-a < 2:
    print('Q')
else:
    print("P")
