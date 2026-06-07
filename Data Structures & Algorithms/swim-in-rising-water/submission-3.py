class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set((0, 0))
        minH = [(grid[0][0], (0, 0))]
        while minH:
            elev, currLoc = heapq.heappop(minH)
            if currLoc[0] == len(grid) - 1 and currLoc[1] == len(grid[0]) - 1:
                return elev
            
            for d in self.DIRECTIONS:
                neighbor = (currLoc[0] + d[0], currLoc[1] + d[1])
                if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or neighbor in visited:
                    continue
                
                visited.add(neighbor)
                heapq.heappush(minH, (max(elev, grid[neighbor[0]][neighbor[1]]), neighbor))

        return -1