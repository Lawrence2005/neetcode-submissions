class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxIdxMap = {}
        for i in range(len(s)):
            maxIdxMap[s[i]] = i

        maxIdxs = []
        for i in range(len(s)):
            maxIdxs.append(maxIdxMap[s[i]])

        result = []
        l, r = 0, 0
        for i in range(len(s)):
            r = max(r, maxIdxs[i])
            if i == r:
                result.append(r - l + 1)
                l = r + 1
                r = l
        return result    