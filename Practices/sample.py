import heapq
class Solution:

    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        
        

        # Create adjacency list representation of the g
        g = {}
        for i in edges:
            u, v, w = i
            # Skip self-loop condition
            if u != v:
                g.setdefault(u, []).append((v, w))
                g.setdefault(v, []).append((u, w))
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0)]  # {distance, node}
        heapq.heapify(pq)
        
        # Initialize distances array with infinity
        d = [float('inf')] * n
        
        while pq:
            dist, curr = heapq.heappop(pq)
            
            # Skip processing if node has already disappeared
            if dist > d[curr] or dist >= disappear[curr]:
                continue
            
            d[curr] = dist
            
            # Traverse neighbors
            neighbors = g.get(curr, [])
            for nextNode, weight in neighbors:
                # Calculate new distance
                newDist = dist + weight
                
                # Update distance if shorter path is found
                if newDist < d[nextNode]:
                    heapq.heappush(pq, (newDist, nextNode))
        
        # Adjust unreachable nodes to -1
        for i in range(n):
            if d[i] == float('inf'):
                d[i] = -1
        
        return d
