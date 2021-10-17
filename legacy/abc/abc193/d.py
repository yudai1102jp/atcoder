k = int(input())
s = (input()[:4]
t=(input())[:4]

ta_s=[0]*10
ao_t=[0]*10


all={i: k for i in range(1, 10)}

for i in range(4):
    ta_s[int(s[i])] += 1
    ao_t[int(t[i])] += 1
    all[int(s[i])] -= 1
    all[int(t[i])] -= 1



taka_win=[[0]*10 for i in range(10)]


def judge(ta, ao):
    sta=0
    sao=0
    for i in range(1, 10):
        sta += i*pow(10, ta[i])
        sao += i*pow(10, ao[i])
    if sta > sao:
        return 1
    else:
        return 0


for i in range(1, 10):
    temp_ta=list(ta_s)
    temp_ta[i] += 1
    for j in range(1, 10):
        if i == j:
            if all[i] < 2:
                continue
        else:
            if all[i] == 0 or all[j] == 0:
                continue
        temp_ao=list(ao_t)
        temp_ao[j] += 1
        taka_win[i][j]=judge(temp_ta, temp_ao)

sum=9*k-8
cho=0
for i in range(1, 10):
    for j in range(1, 10):
        if taka_win[i][j]:
            if i == j:
                cho += all[i]*(all[i]-1)
            else:
                cho += all[i]*all[j]


print(cho/(sum*(sum-1)))
