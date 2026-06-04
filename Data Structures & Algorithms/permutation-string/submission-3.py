class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Count = {}
        for c in s1:
            s1Count[c] = 1 + s1Count.get(c, 0)

        wdwCount = {}
        matches, left = 0, 0
        for right in range(len(s2)):
            wdwCount[s2[right]] = 1 + wdwCount.get(s2[right], 0)
            if s2[right] in s1Count:
                if wdwCount[s2[right]] == s1Count[s2[right]]:
                    matches += 1
                elif wdwCount[s2[right]] == s1Count[s2[right]] + 1:
                    matches -= 1
            
            if matches == len(s1Count):
                return True

            if right - left + 1 < len(s1):
                continue
            
            wdwCount[s2[left]] -= 1
            if s2[left] in s1Count:
                if wdwCount[s2[left]] == s1Count[s2[left]]:
                    matches += 1
                elif wdwCount[s2[left]] == s1Count[s2[left]] - 1:
                    matches -= 1
            left += 1

        return False