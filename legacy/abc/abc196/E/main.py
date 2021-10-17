#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]", t: "List[int]", Q: int, x: "List[int]"):
    fmax = 0
    fmin = 0
    maxinit = False
    mininit = False
    MAX = 10**11
    MIN = -10**11

    degree = 0
    # max
    for i in range(N):
        if t[i] == 1:
            fmax += a[i]
            fmin += a[i]
            degree += a[i]
        elif t[i] == 2:
            if not mininit:
                mininit = True
                fmin = a[i]
            else:
                fmin = max(a[i], fmin)
            fmax = max(a[i], fmax)
            MIN = max(MIN, a[i]-degree)
        elif t[i] == 3:
            if not maxinit:
                maxinit = True
                fmax = a[i]
            else:
                fmax = min(a[i], fmax)
            fmin = min(a[i], fmin)
            MAX = min(MAX, a[i]-degree)

    for i in x:
        if i <= MIN:
            print(fmin)
        elif i >= MAX:
            print(fmax)
        else:
            print(i+degree)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        t[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, a, t, Q, x)


if __name__ == '__main__':
    main()
