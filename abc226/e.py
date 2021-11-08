import typing
import sys
import copy
from collections import deque
import sys  # 追加
sys.setrecursionlimit(500*500)


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


MOD = int(998244353)
N, M = list(map(int, input().split()))
uv = [[int(i) for i in input().split()] for j in range(M)]


if N != M:
    print(0)
    exit()

used = set()

ans = 0

load = [[] for i in range(N)]
union = DSU(N)
for i in range(N):
    load[uv[i][0]-1].append([uv[i][1]-1, i])
    union.merge(uv[i][0]-1, uv[i][1]-1)

    # load[uv[i][1]-1].append([uv[i][0]-1, i])


# for i in range(N):
#     if len(load[i]) == 0:
#         print(0)
#         exit()


def dfs(now,  co, passed, top):
    if co == -1 or now in top:
        return co
    top.add(now)
    co += 1

    for ne in load[now]:
        if co == -1 or ne[1] in passed:
            continue
        passed.add(ne[1])

        co = dfs(ne[0], co, passed, top)
    if co == -1 or len(passed) > len(top):
        return -1
    return co


g = union.groups()
for i in g:
    if sum([len(load[i[j]]) for j in range(len(i))]) == len(i):
        continue
    print(0)
    exit()


# for i in range(N):
#     if i in used:
#         continue
#     top = set()
#     passed = set()
#     co = dfs(i, 0, passed, top)
#     used.update(top)
#     if co == len(passed):
#         ans += 1

#     else:
#         print(0)
#         exit()
print(pow(2, len(g), MOD))
