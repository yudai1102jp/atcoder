import collections

x,y,a,b,c=map(int,input().split())

A=collections.deque(sorted(list(map(int,input().split()))))
B=collections.deque(sorted(list(map(int,input().split()))))
C=collections.deque(sorted(list(map(int,input().split()))))




a_num=A.pop()
b_num=B.pop()
c_num=C.pop()
color_count = [0,0,0]

ans=0
while sum(color_count) < x+y:
    

    
    if max([a_num,b_num,c_num])==a_num :
        ans+=a_num
        color_count[0]+=1
        if A :
            a_num=A.pop()
        if color_count[0]==x:
            a_num=0
    elif max([a_num,b_num,c_num])==b_num :
        ans+=b_num
        color_count[1]+=1
        if B:
            b_num=B.pop()
        
        if color_count[1]==y:
            b_num=0
    else:
        ans+=c_num
        if C:
            c_num=C.pop()
        else:
            c_num=0
        color_count[2]+=1
print(ans)