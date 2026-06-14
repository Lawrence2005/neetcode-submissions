class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        currL, currR = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= currR:
                currL, currR = intervals[i][0], intervals[i][1]
            else:
                currR = min(currR, intervals[i][1])
                count += 1
        return count