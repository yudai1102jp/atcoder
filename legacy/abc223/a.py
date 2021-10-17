# a = list(input())
X = int(input())
# A = list(map(int, input().split()))
# A=[[int(i) for i in input().split()] for j in range(N)]

if X % 100 == 0 and X != 0:
    print('Yes')
else:
    print('No')
