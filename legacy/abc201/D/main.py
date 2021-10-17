
Y,X=map(int,input().split())
map=[[1 if i=='+' else 0 for i in input()] for j in range(Y)]


def cal(x,y,dp):
    if x==X or y==Y:
        return 
    if map[y][x]:
        dp[y][x]+=1
    else:
        dp[y][x]-=1
    cal(x+1,y,dp)
    cal(x,y+1,dp)
    return 

dp=[[0]*X for i in range(Y)]
cal(0,0,dp)
print(dp[Y-1][X-1])
