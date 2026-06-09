class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.adjList = {node: [] for node in range(1, n + 1)}
        for u, v, t in times:
            self.adjList[u].append((v, t))
        
        maxTime, shortest = float('-inf'), [float('inf') for _ in range(n)]
        shortest[k - 1] = 0
        minH = [(0, k)]
        while minH:
            currT, curr = heapq.heappop(minH)
            if currT > shortest[curr - 1]:
                continue
            
            maxTime = max(maxTime, currT)
            for nextNode, t in self.adjList[curr]:
                if currT + t >= shortest[nextNode - 1]:
                    continue
                
                shortest[nextNode - 1] = currT + t
                heapq.heappush(minH, (currT + t, nextNode))
        
        return maxTime if float('inf') not in shortest else -1