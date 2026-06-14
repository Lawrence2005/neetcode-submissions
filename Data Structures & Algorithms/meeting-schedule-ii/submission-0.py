"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [], []
        for intvl in intervals:
            starts.append(intvl.start)
            ends.append(intvl.end)
        starts.sort()
        ends.sort()

        rooms, count = 0, 0
        sIdx, eIdx = 0, 0
        while sIdx < len(starts) or eIdx < len(ends):
            sVal = starts[sIdx] if sIdx < len(starts) else float('inf')
            eVal = ends[eIdx] if eIdx < len(ends) else float('inf')
            if eVal <= sVal:
                count -= 1
                eIdx += 1
            else:
                count += 1
                sIdx += 1
            rooms = max(rooms, count)
        return rooms