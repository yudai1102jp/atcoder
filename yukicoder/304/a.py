N, H, W = map(int, input().split())

n_1 = N//2
n_2 = N-n_1
print((H+W-2)*n_1*n_2)
