#!/usr/bin/env python3
import sys
import copy


def solve(A: int, B: int, C: int):
    A, B, C = sorted([A, B, C], reverse=True)   # A>B>C
    dp = [[[0.0 for k in range(101)] for j in range(101)] for i in range(101)]

    for i in reversed(range(100)):
        dp[99][99][i] = float(i)/(99+99+i) * (dp[99][99][i+1] + 1) + \
            float(99)/(99+99+i) * 2
        dp[i][99][99] = copy.copy(dp[99][99][i])

        dp[99][i][99] = copy.copy(dp[99][99][i])

    for a in reversed(range(100)):
        if a < A:
            break
        for b in reversed(range(100)):
            if b < B:
                break
            for c in reversed(range(100)):
                if c < C:
                    break
                dp[a][b][c] = float(a)/(a+b+c) * (dp[a+1][b][c]+1) + \
                    float(b)/(a+b+c) * (dp[a][b+1][c]+1) + float(c)/(a+b+c) * (dp[a][b][c+1]+1)

    print(dp[A][B][C])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


if __name__ == '__main__':
    main()
