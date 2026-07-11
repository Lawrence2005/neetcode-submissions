class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccur = {}
        for i in range(len(s)):
            lastOccur[s[i]] = i
        
        result = []
        currLast = 0
        l, r = 0, 0
        while r < len(s):
            currLast = max(currLast, lastOccur[s[r]])
            if r == currLast:
                result.append(r - l + 1)
                l = r + 1
            r += 1
        return result