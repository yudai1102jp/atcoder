#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(S: str):

    S_cho = 'chokudai'
    S_li = [0 for _ in S_cho]
    for s in S:
        index_ = S_cho.find(s)
        if index_ >= 0:
            if index_ == 0:
                S_li[0] += 1
            else:
                S_li[index_] += S_li[index_-1]
    print(S_li[-1] % MOD)
    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
