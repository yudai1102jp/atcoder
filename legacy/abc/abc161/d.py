k = int(input())
co = 0
ans = [1, 2]


def checkketa(keta1, keta2):
    if ans[keta1] <= ans[keta2] and ans[keta1] < 9:
        return True
    else:
        return False


def newnum():
    for i in range(len(ans)-1):
        if checkketa(i, i+1):
            new = list(ans)
            new[i] += 1
            for j in range(i, 0, -1):
                if new[j] != 0:
                    new[j-1] = new[j]-1
                else:
                    new[j-1] = 0
            break
    else:
        if ans[-1] != 9:
            new = list(ans)
            new[-1] += 1
            for i in range(len(new)-1,0,-1):
                if new[i]!=0:
                    new[i-1]=new[i]-1
                else:
                    new[i-1]=0
        else:
            new = [0 for i in range(len(ans))]
            new.append(1)

    return new


if (k <= 12):
    print(k)

else:

    for i in range(13, k):

        ans = newnum()

    print(''.join(map(str, reversed(ans))))
