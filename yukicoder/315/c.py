A, B, C, N = map(int, input().split())


dpw = [[[[0 for i in range(51)] for j in range(51)]
        for k in range(51)] for l in range(51)]
dpb = [[[[0 for i in range(51)] for j in range(51)]
        for k in range(51)] for l in range(51)]
dpt = [[[[0 for i in range(51)] for j in range(51)]
        for k in range(51)] for l in range(51)]

dpw[2][0][0][1] = 1
dpb[0][2][0][1] = 1
dpt[0][0][2][1] = 1

for n in range(51):
    for i in range(51):
        for j in range(51):
            for k in range(51):

                S = i+j+k
                wprob = 0
                bprob = 0
                tprob = 0

                next = 0
                if i > 1:
                    wprob = (i*(i-1))/(S*(S-1))
                    next += wprob*dpw[i-1][0][0][1]
                if j > i:
                    bprob = (j*(i-1))/(S*(S-1))
                if k > i:
                    tprob = (k*(i-1))/(S*(S-1))
                oprob = 1-(wprob+bprob+tprob)
                dpw[2][0][0][1] = 1
                dpb[0][2][0][1] = 1
                dpt[0][0][2][1] = 1
