#!/usr/bin/env python3
import sys


def solve(A: "List[int]"):
    a=A[1]-A[0]
    b=A[2]-A[1]
    if a==b:
        print(0)
    else:
        if a>=0:
            pass
        elif b<=0:
            a,b=-b, -a
        if a<b:

            if (b-a)%2==0:
                print((b-a)//2)
            else:
                print(1+(b-a+1)//2)
        elif a>b:
            print(abs(b-a))
        
        


    

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(A)

if __name__ == '__main__':
    main()
