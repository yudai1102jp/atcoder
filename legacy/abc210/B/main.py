#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:

                print('Takahashi')
            else:
                print('Aoki')
            return
    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()
