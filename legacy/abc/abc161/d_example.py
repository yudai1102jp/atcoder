from collections import deque

k = int(input())

q = deque([int(i) for i in range(1,10)])
for i in range(k-1):
    x = q.popleft()
    if x % 10:
        q.append(10*x+x % 10-1)
    q.append(10*x+x % 10)
    if x % 10 != 9:
        q.append(10*x+x % 10+1)

print(q.popleft())
