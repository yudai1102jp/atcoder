h,w=list(map(int,input().split()))
M=1000
S=0
for i in range(h):
    temp=list(map(int,input().split()))
    M=min([min(temp), M])
    S+=sum(temp)

print(S-h*w*M)