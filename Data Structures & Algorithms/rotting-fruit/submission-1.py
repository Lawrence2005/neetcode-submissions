from collections import deque

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.count = 0
        freshCount = 0
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q and freshCount > 0:
            self.count += 1
            qLen = len(q)
            for _ in range(qLen):
                currR, currC = q.popleft()
                for d in self.DIRECTIONS:
                    neighbR, neighbC = currR + d[0], currC + d[1]
                    if not (0 <= neighbR < len(grid) and 0 <= neighbC < len(grid[0])):
                        continue
                    
                    if grid[neighbR][neighbC] != 1:
                        continue
                    
                    grid[neighbR][neighbC] = 2
                    freshCount -= 1

                    q.append((neighbR, neighbC))

        return self.count if freshCount == 0 else -1