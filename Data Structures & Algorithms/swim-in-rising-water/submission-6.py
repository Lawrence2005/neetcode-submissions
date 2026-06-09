class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def swimInWater(self, grid: List[List[int]]) -> int:
        maxLvl = grid[0][0]
        visited = {(0, 0)}
        minH = [(grid[0][0], (0, 0))]
        while minH:
            height, currPos = heapq.heappop(minH)
            maxLvl = max(maxLvl, height)
            if currPos == (len(grid) - 1, len(grid[0]) - 1):
                return maxLvl

            for d in self.DIRECTIONS:
                neighbor = (currPos[0] + d[0], currPos[1] + d[1])
                if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or neighbor in visited:
                    continue
                
                visited.add(neighbor)
                heapq.heappush(minH, (grid[neighbor[0]][neighbor[1]], neighbor))
        
        return maxLvl