# a=map(int, input().split())
# a=input().split()
import copy
N, M = list(map(int, input().split()))

A = [input() for j in range(2*N)]

dp = [[0 for i in range(2*N)] for j in range(M)]
score = [[i, 0] for i in range(2*N)]


def judge(a, b):
    if a == 'G':
        if b == 'C':
            return 0
        elif b == 'P':
            return 1
        else:
            return 2
    elif a == 'C':
        if b == 'P':
            return 0
        elif b == 'G':
            return 1
        else:
            return 2
    elif a == 'P':
        if b == 'G':
            return 0
        elif b == 'C':
            return 1
        else:
            return 2
    else:
        print('error')


now_score = copy.deepcopy(score)

for m in range(M):
    for i in range(N):
        temp = judge(A[now_score[2*i][0]][m], A[now_score[2*i+1][0]][m])
        if temp == 0:
            score[now_score[2*i][0]][1] += 1
        elif temp == 1:
            score[now_score[2*i+1][0]][1] += 1
    now_score = sorted(score, reverse=True, key=lambda x:  x[1])

for i in range(2*N):

    print(now_score[i][0]+1)
