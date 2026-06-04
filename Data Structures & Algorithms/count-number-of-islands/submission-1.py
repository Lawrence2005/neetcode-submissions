from collections import deque
class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '1':
                    continue
                
                self.count += 1
                grid[i][j] = '2'
                self.bfs(grid, (i, j))

        return self.count
    
    def bfs(self, grid, start):
        q = deque([start])
        while q:
            currx, curry = q.popleft()
            for d in self.DIRECTIONS:
                neighbor = (currx + d[0], curry + d[1])
                if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or grid[neighbor[0]][neighbor[1]] != '1':
                    continue
                
                grid[neighbor[0]][neighbor[1]] = '2'
                q.append(neighbor)
        
        return