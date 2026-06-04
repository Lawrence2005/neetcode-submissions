from collections import deque

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                
                grid[i][j] = 2
                self.maxArea = max(self.maxArea, self.getArea(grid, (i, j)))

        return self.maxArea
    
    def getArea(self, grid, start):
        area = 0

        q = deque([start])
        while q:
            currx, curry = q.popleft()
            area += 1
            for d in self.DIRECTIONS:
                neighbor = (currx + d[0], curry + d[1])
                if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or grid[neighbor[0]][neighbor[1]] != 1:
                    continue
                
                grid[neighbor[0]][neighbor[1]] = 2
                q.append(neighbor)
        
        return area