li=[0]*10
len=0
for i in input():
    len+=1
    li[int(i)]+=1




def check(li):
    for i in range(1,10,2):
        
        if li[i]:
            temp_li=list(li)
            temp_li[i]-=1
            if temp_li[1] and temp_li[2]:
                return True
            elif temp_li[2] and temp_li[8]:
                return True
            elif temp_li[3] and temp_li[6]:
                return True
            elif temp_li[4] and temp_li[4]:
                return True
            elif temp_li[5] and temp_li[2]:
                return True
            elif temp_li[6] and temp_li[8]:
                return True
            elif temp_li[7] and temp_li[6]:
                return True
            elif temp_li[8] and temp_li[4]:
                return True
            elif temp_li[9] and temp_li[2]:
                return True
    for i in range(2,9,2):
        if li[i]:
            temp_li=list(li)
            temp_li[i]-=1
            if temp_li[1] and temp_li[6]:
                return True
            elif temp_li[2] and temp_li[4]:
                return True
            elif temp_li[3] and temp_li[2]:
                return True
            elif temp_li[4] and temp_li[8]:
                return True
            elif temp_li[5] and temp_li[6]:
                return True
            elif temp_li[6] and temp_li[4]:
                return True
            elif temp_li[7] and temp_li[2]:
                return True
            elif temp_li[8] and temp_li[8]:
                return True
            elif temp_li[9] and temp_li[6]:
                return True 

    return False


def check2(li):
    temp_li = list(li)
    if temp_li[1] and temp_li[6]:
        return True
    elif temp_li[2] and temp_li[4]:
        return True
    elif temp_li[3] and temp_li[2]:
        return True
    elif temp_li[4] and temp_li[8]:
        return True
    elif temp_li[5] and temp_li[6]:
        return True
    elif temp_li[6] and temp_li[4]:
        return True
    elif temp_li[7] and temp_li[2]:
        return True
    elif temp_li[8] and temp_li[8]:
        return True
    elif temp_li[9] and temp_li[6]:
        return True
    else:
        return False


if len>=3:
    if check(li):
        print('Yes')
    else:
        print('No')
elif len==2:
    if check2(li):
        print('Yes')
    else:
        print('No') 
elif len==1:
    if li[8]:
        print("Yes")
    else:
        print("No")