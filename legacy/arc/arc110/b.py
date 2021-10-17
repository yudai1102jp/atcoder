n=int(input())
t=input()
if (n==1):
    if t=='1':
        print(int(2*1e10))
    if t == '0':
        print(int(1e10))
elif (n==2):
    if t=='11' or t=='10' :
        print(int(1e10))
    elif t=='01':
        print(int(1e10-1))
    elif t=='00':
        print(0)

elif '010' in t or '00' in t or '111' in t:
    print(0)
    
else:
     
    
    
    zero=t.count('0')
    if (t[-1])=='0':
        print(int(1e10-zero+1))
    else:
        print(int(1e10-zero))
    

