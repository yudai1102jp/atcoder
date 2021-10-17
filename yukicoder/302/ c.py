import math
A = int(input())

B = input()
L = len(B)-1
B = int(B, A)

MOD = 10**9+7

# logB = int(math.log(B, A))
ans = (B+1)*L % MOD

minus = 0
now = A
for i in range(1, 1+L):
    minus = (minus + now) % MOD
    now = (now*A) % MOD

print((ans-minus) % MOD)
