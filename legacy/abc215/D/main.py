#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]"):

    A_list = [False]*(10**5+3)
    kouho = [True]*(10**5+3)
    isprime = [True]*(10**5+3)
    except_prime = []

    for i in A:
        A_list[i] = True
        if i <= M:
            kouho[i] = False
    for p in range(2, 10**5+3):
        if not isprime[p]:
            continue
        for i in range(p*2, 10**5+3, p):
            if A_list[i]:
                except_prime.append(p)
            isprime[i] = False

    for p in except_prime:
        if p <= M and kouho[p]:

            kouho[p] = False
            for i in range(p*2, M+1, p):
                kouho[i] = False
    kouho[1] = True
    pri = [i for i in range(1, M+1) if kouho[i]]
    print(len(pri))
    for i in pri:
        print(i)

        # Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()