#!/usr/bin/env python3
import sys
import heapq


def solve(N: int, M: int, A: "List[int]"):
    heapq.heapify(A)

    while M:
        heapq.heappush(A, ((heapq.heappop(A)*-1)//2)*-1)
        M -= 1
    ans = 0

    print(-sum(A))

    # dp = [0]*(N+1)
    # used = 0

    # ans = 0
    # for i in range(1, N):
    #     temp = 0
    #     while A[i-1]/pow(2, temp) > A[i] and used+i <= M:
    #         temp += 1
    #         used += i
    #         dp[i] += 1

    #     dp[i+1] = dp[i]

    # dp[N] += (M-used)//N
    # used += ((M-used)//N)*N

    # two = 0

    # for i in range(1, N+1):
    #     temp = A[i-1]//pow(2, dp[N]-dp[i-1])
    #     if used < M and temp > 2:
    #         used += 1
    #         ans += A[i-1]//pow(2, dp[N]-dp[i-1]+1)
    #     else:
    #         ans += temp
    #     if temp == 2 or temp == 1:
    #         two += 1

    # if M-used:
    #     ans -= min(two, M-used)

    # if ans < 0:
    #     print(0)
    # else:
    #     print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    N, M = map(int, input().split())  # type: int

    A = [int(i)*-1 for i in input().split()]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()