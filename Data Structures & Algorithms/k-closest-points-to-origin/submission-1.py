import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), i) for i in range(len(points))]
        heapq.heapify(distances)

        result = []
        for i in range(k):
            p = heapq.heappop(distances)
            result.append(points[p[1]])

        return result