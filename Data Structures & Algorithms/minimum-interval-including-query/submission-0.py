class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q_sorted = sorted((q, i) for i, q in enumerate(queries))

        minH = []
        result, iIdx = [-1 for _ in range(len(queries))], 0
        for q, i in q_sorted:
            while iIdx < len(intervals) and intervals[iIdx][0] <= q:
                heapq.heappush(minH, (intervals[iIdx][1] - intervals[iIdx][0] + 1, intervals[iIdx][1]))
                iIdx += 1

            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            if minH:
                result[i] = minH[0][0]
        return result