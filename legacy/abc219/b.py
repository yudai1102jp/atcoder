
T = []
for i in range(3):
    T.append(input())
t = input()
a = []
for i in t:
    a.append(T[int(i)-1])
print(''.join(a))
