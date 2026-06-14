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
        for p in self.pts:
            xDiff, yDiff = point[0] - p[0], point[1] - p[1]
            if abs(xDiff) != abs(yDiff) or abs(xDiff) == 0:
                continue

            count += self.pMap.get((p[0], point[1]), 0) * self.pMap.get((point[0], p[1]), 0)
        return count