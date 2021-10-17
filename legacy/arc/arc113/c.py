s = input()

N = len(s)

si_2 = s[-1]
si_1 = s[-2]
last = N-2
ans = 0
str_dic = {chr(i): 0 for i in range(97, 123)}

str_dic[si_2]+=1
for i in reversed(range(N-2)):
    si = s[i]
    if si_1 == si and si != si_2:

        ans += last-i-str_dic[si]
        str_dic = {chr(i): 0 for i in range(97, 123)}
        str_dic[si] = N-i-1
    else:
        str_dic[si_1] += 1

    si_1, si_2 = si, si_1
print(ans)
