#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    N = int(input())
    S = input()
    Q = int(input())

    for q in range(Q):
        tab = list(map(int, input().split()))
        if tab[0] == 1:
            a = tab[1]-1
            b = tab[2]-1
            if b+1==2*N:
                S = S[:a]+S[b]+S[a+1:b]+S[a]
            else:
                S = S[:a]+S[b]+S[a+1:b]+S[a]+S[b+1:]
        else:
            S=S[N:]+S[:N]
    print(S)

    return


if __name__ == '__main__':
    main()
