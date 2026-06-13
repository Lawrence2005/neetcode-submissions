class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        currL, currR = newInterval[0], newInterval[1]
        while i < len(intervals) and intervals[i][0] <= currR:
            currL = min(currL, intervals[i][0])
            currR = max(currR, intervals[i][1])
            i += 1
        result.append((currL, currR))
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
            
        return result