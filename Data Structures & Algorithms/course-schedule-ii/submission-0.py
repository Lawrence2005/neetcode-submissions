from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees, nexts = {c: 0 for c in range(numCourses)}, [[] for c in range(numCourses)]
        for c, prec in prerequisites:
            inDegrees[c] += 1
            nexts[prec].append(c)
        
        order = self.helper(inDegrees, nexts)

        return order if len(order) == numCourses else []
    
    def helper(self, inD, nexts):
        result = []

        q = deque([])
        for c in inD:
            if inD[c] == 0:
                q.append(c)
        
        while q:
            c = q.popleft()
            result.append(c)

            for nextC in nexts[c]:
                inD[nextC] -= 1
                if inD[nextC] == 0:
                    q.append(nextC)
        
        return result
