

N, Q = list(map(int, input().split()))


class Node:
    def __init__(self, n) -> None:
        self.n = n
        self.mae = None
        self.usiro = None


# class Head:
#     def __init__(self) -> None:
HEAD = []
for i in range(N+1):
    HEAD.append(Node(i))


for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        HEAD[q[1]].usiro = HEAD[q[2]]
        HEAD[q[2]].mae = HEAD[q[1]]
    elif q[0] == 2:
        HEAD[q[1]].usiro = None
        HEAD[q[2]].mae = None
    else:
        node = HEAD[q[1]]
        while True:
            if node.mae == None:
                break
            node = node.mae

        ans = []
        while True:
            ans.append(node.n)
            if node.usiro == None:
                break
            node = node.usiro
        print(len(ans), *ans)
