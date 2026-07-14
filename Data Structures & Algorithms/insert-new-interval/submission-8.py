class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] >= newInterval[0]:
                break
            
            result.append(intervals[i])
            i += 1

        toInsert = [min(intervals[i][0], newInterval[0]), newInterval[1]] if i < len(intervals) else newInterval
        while i < len(intervals):
            if intervals[i][0] > toInsert[1]:
                break
            
            toInsert[1] = max(toInsert[1], intervals[i][1])
            i += 1
        result.append(toInsert)
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result