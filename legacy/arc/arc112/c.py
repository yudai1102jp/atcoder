n=int(input())
p=list(map(int,input().split()))

root={i:[set(),1] for i in range(1,n+1)}
for i in range(n-1):
    root[p[i]][0].add(i+2)





print(root)