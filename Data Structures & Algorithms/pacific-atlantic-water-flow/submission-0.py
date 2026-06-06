from collections import deque

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pq, aq = deque([]), deque([])
        pVisited, aVisited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))], [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        for i in range(len(heights[0])):
            pq.append((0, i))
            aq.append((len(heights) - 1, i))

            pVisited[0][i] = True
            aVisited[len(heights) - 1][i] = True
        for j in range(len(heights) - 1):
            pq.append((1 + j, 0))
            aq.append((len(heights) - 2 - j, len(heights[0]) - 1))

            pVisited[1 + j][0] = True
            aVisited[len(heights) - 2 - j][len(heights[0]) - 1] = True

        pSet = set()
        while pq:
            currR, currC = pq.popleft()
            pSet.add((currR, currC))
            for d in self.DIRECTIONS:
                neighbR, neighbC = currR + d[0], currC + d[1]
                if not (0 <= neighbR < len(heights) and 0 <= neighbC < len(heights[0])) or pVisited[neighbR][neighbC]:
                    continue
                
                if heights[neighbR][neighbC] < heights[currR][currC]:
                    continue
                
                pVisited[neighbR][neighbC] = True
                pq.append((neighbR, neighbC))
        
        aSet = set()
        while aq:
            currR, currC = aq.popleft()
            aSet.add((currR, currC))
            for d in self.DIRECTIONS:
                neighbR, neighbC = currR + d[0], currC + d[1]
                if not (0 <= neighbR < len(heights) and 0 <= neighbC < len(heights[0])) or aVisited[neighbR][neighbC]:
                    continue
                
                if heights[neighbR][neighbC] < heights[currR][currC]:
                    continue
                
                aVisited[neighbR][neighbC] = True
                aq.append((neighbR, neighbC))
        
        return [[coord[0], coord[1]] for coord in pSet & aSet]