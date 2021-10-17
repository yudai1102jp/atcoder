N = int(input())

user = set()
for i in range(N):
    s = input()
    if s in user:
        continue
    else:
        user.add(s)
        print(i+1)
