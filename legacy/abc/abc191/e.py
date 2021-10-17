n, m = map(int, input().split())
dec = [i:[] for i in range(1, n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    dec[a].append([b, c])



for i in range(n):
    Set=set()
    next =  dec[i]
    while next:
        for ne in next:


        
