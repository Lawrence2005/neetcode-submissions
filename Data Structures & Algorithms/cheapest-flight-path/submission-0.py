from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.adjList = {airport: [] for airport in range(n)}
        for a1, a2, p in flights:
            self.adjList[a1].append((a2, p))
        
        cheapest = [float('inf') for _ in range(n)]
        cheapest[src] = 0
        stops = 0
        q = deque([(0, src)])
        while q and stops <= k:
            stops += 1
            temp = cheapest
            for _ in range(len(q)):
                cost, curr = q.popleft()
                for nextA, p in self.adjList[curr]:
                    if cost + p >= temp[nextA]:
                        continue
                    
                    temp[nextA] = cost + p
                    q.append((cost + p, nextA))
            cheapest = temp
        
        return cheapest[dst] if cheapest[dst] != float('inf') else -1