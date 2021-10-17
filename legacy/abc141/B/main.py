#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(s: str):
    for i in range(len(s)):
        if i % 2 == 1:
            if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
                continue
        if i % 2 == 0:
            if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
                continue
        print('No')
        return
    print("Yes")
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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