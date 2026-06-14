class CountSquares:

    def __init__(self):
        self.pMap = {}
        self.pts = []

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.pMap:
            self.pMap[tuple(point)] = 0
        self.pMap[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point[0], point[1]
        for p in self.pts:
            if abs(px - p[0]) != abs(py - p[1]) or abs(px - p[0]) == 0:
                continue
            
            count += self.pMap.get((px, p[1]), 0) * self.pMap.get((p[0], py), 0)
        return count