k = int(input())

p = 1/k


dp = [0]*k
dp[1] = k
su = k
for i in range(2, k):
    dp[i] = dp[i-1]+(k/i)

print(dp[k-1])
