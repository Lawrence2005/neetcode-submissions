from collections import deque

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def swimInWater(self, grid: List[List[int]]) -> int:
        left, right = float('inf'), float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left, right = min(left, grid[i][j]), max(right, grid[i][j])
        
        answer = float('inf')
        while left <= right:
            middle = left + (right - left) // 2
            if self.helper(grid, middle):
                answer = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return answer
    
    def helper(self, grid, wLvl):
        if grid[0][0] > wLvl:
            return False
            
        q = deque([(0, 0)])
        visited = set((0, 0))
        while q:
            currLoc = q.popleft()
            if currLoc == (len(grid) - 1, len(grid[0]) - 1):
                return True

            for d in self.DIRECTIONS:
                neighbor = (currLoc[0] + d[0], currLoc[1] + d[1])
                if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or neighbor in visited:
                    continue
                
                if grid[neighbor[0]][neighbor[1]] > wLvl:
                    continue
                
                visited.add(neighbor)
                q.append(neighbor)
        
        return False

