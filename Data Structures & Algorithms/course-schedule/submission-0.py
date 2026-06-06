from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap, prereqCounts = {c: set() for c in range(numCourses)}, {c: 0 for c in range(numCourses)}
        for c, prec in prerequisites:
            prereqMap[prec].add(c)
            prereqCounts[c] += 1
        
        q = deque([])
        for c in prereqCounts:
            if prereqCounts[c] == 0:
                q.append(c)
        
        completed = 0
        while q:
            c = q.popleft()
            completed += 1
            for nextC in prereqMap[c]:
                prereqCounts[nextC] -= 1
                if prereqCounts[nextC] == 0:
                    q.append(nextC)
        
        return completed == numCourses