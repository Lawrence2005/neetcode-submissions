class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        currL, currR = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if currR < intervals[i][0]:
                result.append([currL, currR])
                currL = intervals[i][0]
            currR = max(currR, intervals[i][1])
        result.append([currL, currR])
        return result