def matrix():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                

n = int(input())

xy = []
for i in range(n):

    xy.append(np.array([int(i) for i in input().split()]+[1]))

m = int(input())

op = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
op1 = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
op2 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
for i in range(m):
    temp = input().split()

    if(temp[0] == 1):
        op.append(op[-1]*op1j)
    if(temp[0] == 2):
        op.append(op[-1]*op2)
    if(temp[0] == 3):
        op.append(op[-1]*np.array([[1, 0, int(temp[1])], [0, 1, 0], [0, 0, 1]])
                  * np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    if(temp[0] == 2):
        op.append(op[-1]*np.array([[1, 0, 0], [0, 1, int(temp[1])], [0, 0, 1]])
                  * np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]]))


q = int(input())

for i in range(q):

    a, b = map(int, input().split())

    temp = op[a]*xy[b-1]
    print(str(temp[0])+' '+str(temp[1]))
