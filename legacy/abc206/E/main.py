#!/usr/bin/env python3
import sys
import sympy


def solve(L: int, R: int):
    if R <= 5:
        print(0)
        return
    ans = 0
    for i in range(L, R+1):
        if sympy.isprime(i):
            continue
        f = sympy.factorint()
        for key, v in f.items():
            ans =

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)


if __name__ == '__main__':
    main()
