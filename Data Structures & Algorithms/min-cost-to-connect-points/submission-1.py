class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {p: [] for p in range(len(points))}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        cost = 0
        visited = set()
        minH = [(0, 0)]
        while len(visited) < len(points):
            dist, pIdx = heapq.heappop(minH)
            if pIdx in visited:
                continue
            
            visited.add(pIdx)
            cost += dist
            for d, neighbor in adjList[pIdx]:
                heapq.heappush(minH, (d, neighbor))
        
        return cost