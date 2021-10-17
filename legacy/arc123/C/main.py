

for i in range(int(input())):
    case=(input())
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
    print(ans)
  