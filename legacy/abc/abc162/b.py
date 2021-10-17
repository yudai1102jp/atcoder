n=int(input())

ans=sum([int(i) for i in range(n+1) if i %3 and i%5])
print(ans)