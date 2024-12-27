from typing import List
import heapq

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = {}
        for i in edges:
            u, v, time = i
            if u not in g:
                g[u] = []
            if v not in g:
                g[v] = []
            g[u].append((v, time))
            g[v].append((u, time))

        pq = [(0, 0)]  # [(node, time)]
        heapq.heapify(pq)

        a = [-1] * n

        while pq:
            c = heapq.heappop(pq)
            node, time = c
            if a[node] != -1:
                continue

            a[node] = time
            if node in g:
                for ne in g[node]:
                    nn, nextTime = ne
                    if a[nn] == -1 and time + nextTime < disappear[nn]:
                        heapq.heappush(pq, (nn, time + nextTime))

        return a
