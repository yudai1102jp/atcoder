
def YES():
    print('Yes')


def NO():
    print('No')


def TAKAHASHI():
    print('Takahashi')


def AOKI():
    print("Aoki")


MOD = int(1e9+7)
s = (input())
# N = int(input())
# A = list(map(int, input().split()))
# A = [[int(i) for i in input().split()] for j in range(N)]

ans = {}

if s[0] == s[1] == s[2]:
    print(1)


elif s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
    print(3)
else:
    print(6)
