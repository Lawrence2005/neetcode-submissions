from collections import deque

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            currR, currC, dist = q.popleft()
            
            for d in self.DIRECTIONS:
                neighborR, neighborC = currR + d[0], currC + d[1]
                if not (0 <= neighborR < len(grid) and 0 <= neighborC < len(grid[0])):
                    continue
                
                if grid[neighborR][neighborC] == 0 or grid[neighborR][neighborC] == -1:
                    continue
                
                if dist + 1 > grid[neighborR][neighborC]:
                    continue
                
                grid[neighborR][neighborC] = dist + 1
                q.append((neighborR, neighborC, dist + 1))
        
        return