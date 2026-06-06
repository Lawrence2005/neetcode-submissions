from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees, nexts = {c: 0 for c in range(numCourses)}, {c: set() for c in range(numCourses)}
        for c, preC in prerequisites:
            inDegrees[c] += 1
            nexts[preC].add(c)
        
        order = self.helper(inDegrees, nexts)

        return len(order) == numCourses
    
    def helper(self, inD, nexts):
        q = deque([])
        for c in inD:
            if inD[c] == 0:
                q.append(c)
        
        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for nextC in nexts[c]:
                inD[nextC] -= 1
                if inD[nextC] == 0:
                    q.append(nextC)
        
        return result
