from collections import deque


def next_num():
    for s1 in range(4):
        for s2 in range(4):
            for s3 in range(1, 4):
                num = pow(10, 2)*s1+pow(10, 1)*s2+s3
                yield num

for i in range(1000):
    case = str(i)
    ans=1
    while True:
        
        for s in case:
            if ans==1:
                if not 0<int(s)<=3:
                    ans=4 if s=='0'  else (int(s)+2)//3

                    
            elif ans==2:
                if not 2<=int(s)<=6:
                    ans=4 if s=='0' or s=='1' else (int(s)+2)//3
                    
            elif ans==3:
                if not 3<=int(s)<=9:
                    ans=4
                    

        else:
            break



    q=deque()
    now=[i, [],0]
    while now[0]>0:

        num_gen=next_num()
        for num in num_gen:
            if num==now[0]:
                # print(i, now[1]+[num], now[2]+1)
                q.appendleft([now[0]-num, now[1]+[num], now[2]+1]) 

                break
            elif num>now[0]:
                break
            else:
                q.append([now[0]-num, now[1]+[num], now[2]+1]) 
    
        
        now=q.popleft()
    if ans !=now[2]:
        print(i , now[1:])




