from collections import deque

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.pSet, self.aSet = set(), set()
        self.pq, self.aq = deque([]), deque([])
        self.pVisited, self.aVisited = set(), set()
        for i in range(len(heights[0])):
            self.pq.append((0, i))
            self.pVisited.add((0, i))
            self.aq.append((len(heights) - 1, i))
            self.aVisited.add((len(heights) - 1, i))
        for j in range(len(heights) - 1):
            self.pq.append((j + 1, 0))
            self.pVisited.add((j + 1, 0))
            self.aq.append((len(heights) - 2 - j, len(heights[0]) - 1))
            self.aVisited.add((len(heights) - 2 - j, len(heights[0]) - 1))
        
        self.helper(heights, self.pq, self.pVisited, self.pSet)
        self.helper(heights, self.aq, self.aVisited, self.aSet)
        return [[coord[0], coord[1]] for coord in self.pSet & self.aSet]
        
    def helper(self, heights, q, visited, result):
        while q:
            currPos = q.popleft()
            result.add(currPos)
            for d in self.DIRECTIONS:
                neighbor = (currPos[0] + d[0], currPos[1] + d[1])
                if not (0 <= neighbor[0] < len(heights) and 0 <= neighbor[1] < len(heights[0])) or neighbor in visited:
                    continue

                if heights[neighbor[0]][neighbor[1]] < heights[currPos[0]][currPos[1]]:
                    continue
                
                visited.add(neighbor)
                q.append(neighbor)
        return