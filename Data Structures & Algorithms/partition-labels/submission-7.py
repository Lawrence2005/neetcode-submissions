class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccur = {}
        for i in range(len(s)):
            lastOccur[s[i]] = i
        
        result = []
        l, r = 0, 0
        for i in range(len(s)):
            r = max(r, lastOccur[s[i]])
            if i == r:
                result.append(i - l + 1)
                l = r + 1
        return result