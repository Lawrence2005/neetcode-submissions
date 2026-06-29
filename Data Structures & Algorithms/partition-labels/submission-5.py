class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccur = {}
        for i in range(len(s)):
            lastOccur[s[i]] = i
        
        result = []
        farthest = 0
        prev, curr = -1, 0
        while curr < len(s):
            farthest = max(farthest, lastOccur[s[curr]])
            if curr == farthest:
                result.append(curr - prev)
                prev = curr
            curr += 1
        return result