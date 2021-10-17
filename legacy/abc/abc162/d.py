n = int(input())
s = input()
ans = 0
R=[]
G=[]
B =[]
for i in range(n):
    if s[i]=='R':
        R.append(i)
    if s[i]=='G':
        G.append(i)
    if s[i]=='B':
        B.append(i)

ans=len(R)*len(G)*len(B)


for i in range(n):
    for j in range(i+1,n):
        if 2*j-i<n:

            if  len(set([s[i],s[j],s[2*j-i]]))==3:
                ans-=1
        else:
            break

print(ans)
