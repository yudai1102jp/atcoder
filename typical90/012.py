from collections import deque
import typing


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


H, W = map(int, input().split())
Q = int(input())


grid = [[0 for i in range(W)] for j in range(H)]
dsu = DSU(W*H+6)
for i in range(Q):
    q = list(map(lambda x: int(x)-1, input().split()))
    if q[0] == 0:
        r, c = q[1:]
        grid[r][c] = 1
        for closed in [[0, 1], [0, -1], [1, 0], [-1, 0]]:

            ny = r+closed[0]
            nx = c+closed[1]
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx]:
                dsu.merge(r*W+c, ny*W+nx)

    else:
        ra, ca, rb, cb = q[1:]
        if grid[ra][ca] == 1 and grid[rb][cb] == 1 and dsu.same(ra*W+ca, rb*W+cb):
            print('Yes')

        else:
            print('No')
