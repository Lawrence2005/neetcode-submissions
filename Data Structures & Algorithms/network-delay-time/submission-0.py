from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.adjList = {node: [] for node in range(n + 1)}
        for u, v, t in times:
            self.adjList[u].append((v, t))

        maxTime, shortest = float('-inf'), [float('inf') for node in range(n)]
        shortest[k - 1] = 0
        minHeap = [(0, k)]
        while minHeap:
            currT, curr = heapq.heappop(minHeap)
            if currT > shortest[curr - 1]:
                continue

            maxTime = max(maxTime, currT)
            for neighbor, t in self.adjList[curr]:
                if currT + t >= shortest[neighbor - 1]:
                    continue
                
                shortest[neighbor - 1] = min(shortest[neighbor - 1], currT + t)
                heapq.heappush(minHeap, (currT + t, neighbor))
        
        return maxTime if float('inf') not in shortest else -1