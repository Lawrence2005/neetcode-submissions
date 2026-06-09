class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest = [float('inf') for _ in range(n)]
        cheapest[src] = 0

        for _ in range(k + 1):
            updated = False
            tmp = cheapest[:]
            for a1, a2, p in flights:
                if cheapest[a1] == float('inf'):
                    continue
                
                if tmp[a2] > cheapest[a1] + p:
                    tmp[a2] = cheapest[a1] + p
                    updated = True
            
            if not updated:
                break
            
            cheapest = tmp
        
        return cheapest[dst] if cheapest[dst] != float('inf') else -1