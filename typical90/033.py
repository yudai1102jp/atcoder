
H, W = map(int, input().split())
if H > 1 and W > 1:
    print(((H+1)//2)*((W+1)//2))
else:
    print(H*W)
