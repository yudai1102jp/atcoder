import sys
import math
from heapq import heappop, heappush
sys.setrecursionlimit(2500000)


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def dijkstra(nodes):
    start_node = nodes[0]
    routes_from_start = {n: math.inf for n in nodes}

    # 最初の頂点にゼロを設定
    routes_from_start[start_node] = 0

    minHeap = []

    # 最初の頂点を追加
    heappush(minHeap, (0, start_node))

    # ヒープがなくなるまで探索
    while minHeap:
        (cost, current_node) = heappop(minHeap)

        # priority keyは重複するのでここでチェックする
        if cost > routes_from_start[current_node]:
            continue

        for node in current_node.routes:
            price_info = current_node.routes[node]
            if routes_from_start[node] > price_info + routes_from_start[current_node]:
                routes_from_start[node] = price_info + routes_from_start[current_node]
                # 更新されたらpriorityに値を追加
                heappush(minHeap, (price_info + routes_from_start[current_node], node))

    return routes_from_start[nodes[-1]]
  1

N = I()
A = [LI() for _ in range(N)]

def cal(a, b,):  # 拡張ユークリッド互助法（不定１次方程式の特殊解）　// ax + by = gcd(a, b)

    if (b == 0):
        x = 1
        y = 0
        return a, y, x

    d, x1, y1 = cal(b, a % b)
    y1 -= a//b * x1
    return d, y1, x1


a, y1, x1 = (cal(111, 30))

print(f"x*a+y*b={x1*b1+-1*y1*b2}")
print(f"a2-a1={a2-a1}")
