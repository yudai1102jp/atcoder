x,y,a,b,c=map(int,input().split())

A=sorted(list(map(int,input().split())), reverse=True)[:x]
B=sorted(list(map(int,input().split())), reverse=True)[:y]
C=list(map(int,input().split()))

print(sum([i for i in sorted(A+B+C, reverse=True)][:x+y]))