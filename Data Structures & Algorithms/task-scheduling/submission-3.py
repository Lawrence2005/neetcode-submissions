from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tCounts = [0 for _ in range(26)]
        for t in tasks:
            tCounts[ord(t) - ord('A')] += 1
        
        heap = []
        for t in tCounts:
            if t > 0:
                heapq.heappush(heap, -t)
        
        time = 0
        q = deque([])
        while heap or q:
            time += 1
            if heap:
                curr = heapq.heappop(heap)

                newCurr = curr + 1
                if newCurr != 0:
                    q.append((newCurr, time + n))
            
            if q and q[0][1] == time:
                available = q.popleft()
                heapq.heappush(heap, available[0])

        return time