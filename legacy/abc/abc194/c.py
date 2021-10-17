n = int(input())

A = [int(i) for i in input().split()]
sq = [i*i for i in A]
Aco = {i: 0 for i in range(-200, 201)}
for i in A:
    Aco[i] += 1
ans = sum(sq)*(n-1)
su = 0
for i in range(-200, 201):
    for j in range(-200, 201):
        if Aco[i] and  Aco[j]:
            

            if i == j :
                su += i*i*Aco[i]*(Aco[i]-1)
            else:
                su += i*j*Aco[i]*Aco[j]
print(ans-su)
