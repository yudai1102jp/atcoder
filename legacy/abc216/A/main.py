#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format

    X, Y = map(int, input().split('.'))

    if 0 <= Y <= 2:
        print(f'{X}-')
    elif 3 <= Y <= 6:
        print(f'{X}')
    else:
        print(f'{X}+')


if __name__ == '__main__':
    main()
