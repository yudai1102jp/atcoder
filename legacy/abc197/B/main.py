#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    h, w, x, y = map(int, input().split())
    s = [input() for i in range(h)]
    ans = 0
    fx = True
    fy = True
    fx_ = True
    fy_ = True
    for i in range(1, max(h, w)):

        if fx and x-i-1 >= 0 and s[x-i-1][y-1] == '.':
            ans += 1
        else:
            fx = False
        if fx_ and x+i-1 < h and s[x+i-1][y-1] == '.':
            ans += 1
        else:
            fx_ = False
        if fy and y-i-1 >= 0 and s[x-1][y-i-1] == '.':
            ans += 1
        else:
            fy = False
        if fy_ and y+i -1< w and s[x-1][y+i-1] == '.':
            ans += 1
        else:
            fy_ = False
    print(ans+1)
    # Failed to predict input format


if __name__ == '__main__':
    main()
