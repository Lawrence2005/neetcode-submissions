class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.adjList = {p: [] for p in range(len(points))}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if i == j:
                    continue
                
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                self.adjList[i].append((j, dist))
                self.adjList[j].append((i, dist))
        
        cost = 0
        visited = set()
        minH = [(cost, 0)]
        while len(visited) != len(points):
            dist, curr = heapq.heappop(minH)
            if curr in visited:
                continue
            
            cost += dist
            visited.add(curr)
            for i in range(len(self.adjList[curr])):
                if self.adjList[curr][i][0] in visited:
                    continue
                
                heapq.heappush(minH, (self.adjList[curr][i][1], self.adjList[curr][i][0]))
        
        return cost