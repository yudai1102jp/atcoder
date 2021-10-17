# a = list(input())
N = int(input())
# A = list(map(int, input().split()))
AB = [[int(i) for i in input().split()] for j in range(N)]

long = 0
for i in range(N):
    long += AB[i][0]/AB[i][1]
t = long/2
now_t = 0
ans = 0
for i in range(N):
    if t > AB[i][0]/AB[i][1]:
        t -= AB[i][0]/AB[i][1]
        ans += AB[i][0]
    else:
        print(ans+t*AB[i][1])
        break
