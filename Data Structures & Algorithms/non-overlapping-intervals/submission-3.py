class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        removals = 0
        currR = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= currR:
                currR = intervals[i][1]
            else:
                currR = min(currR, intervals[i][1])
                removals += 1
        return removals