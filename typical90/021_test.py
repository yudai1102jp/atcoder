import copy
import sys
import typing


class CSR:
    def __init__(
            self, n: int, edges: typing.List[typing.Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = copy.deepcopy(self.start)
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class SCCGraph:
    '''
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    '''

    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []

    def num_vertices(self) -> int:
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups


N, M = map(int, input().split())

scc = SCCGraph(N)

# allow = [set() for i in range(N)]
# non_check = set()
for i in range(M):
    a, b = map(int, input().split())
    scc.add_edge(a-1, b-1)
    # allow[a-1].add(b-1)
    # non_check.add(a-1)

# print(scc.scc())
# loop = [set()]
# check = set()
# temp = set()
# ans = 0

# check = set()
# for i in range(N):
#     while allow[i]:
#         now = allow[i].pop()
#         if i in allow[now]:
#             ans += 1
# allow[now].rempve(i)
# print(ans)

# for a in allow[now]:
#     if now in allow[a]:
#         ans+=1
#         allow[now].pop(a)
#         allow[a].pop(now)
#     else:
#         allow[now]


# def Loop(start, now_check):

#     for next in allow[start]:
#         if next == goal:
#             global loop
#             loop[loop_n] = loop[loop_n] | now_check | set([start])
#             continue
#         if next in now_check:
#             global temp
#             temp.add(start)
#             continue
#         if next not in non_check:
#             continue
#         Loop(next, now_check | set([start]))


# goal = 0
# loop_n = 0
# while non_check:
#     t = non_check.pop()
#     temp.add(t)
#     non_check.add(t)

#     while temp:
#         goal = temp.pop()
#         Loop(goal, set([goal]))
#     non_check = non_check-loop[loop_n]-set([t])
#     goal += 1
#     loop_n += 1
#     loop.append(set())

# ans = 0
# for i in loop:
#     ans += len(i)*(len(i)-1)//2
# print(ans)

ans = 0
for i in scc.scc():
    if len(i)-1:
        ans += (len(i)*(len(i)-1))//2
print(ans)
