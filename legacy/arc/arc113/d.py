n,m,k=map(int,input().split())
MOD = 998244353
ans=pow(k,m,MOD)  
ans+=k*(k-1) 
