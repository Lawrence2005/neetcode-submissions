class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.count += 1

                    self.dfs(grid, (i, j))
        return self.count
    
    def dfs(self, grid, currPos):
        grid[currPos[0]][currPos[1]] = '2'

        for d in self.DIRECTIONS:
            neighbor = (currPos[0] + d[0], currPos[1] + d[1])
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or grid[neighbor[0]][neighbor[1]] != '1':
                continue
            
            self.dfs(grid, neighbor)
        
        return