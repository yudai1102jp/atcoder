n = int(input())
s = input()
x = input()
dp = [False]*7
dp[0] = True
ten = 1
for i in reversed(range(n)):
    old = list(dp)

    for j in range(7):
        nj = (j+int(s[i])*ten) % 7
        if x[i] == 'T':

            dp[j] = old[j] or old[nj]
        else:
            dp[j] = old[j] and old[nj]
    ten = (ten*10) % 7

if dp[0]:
    print("Takahashi")
else:
    print("Aoki")
