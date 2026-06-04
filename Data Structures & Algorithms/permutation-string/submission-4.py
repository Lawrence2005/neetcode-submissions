class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Counts = {}
        for c in s1:
            s1Counts[c] = 1 + s1Counts.get(c, 0)
        
        wdwCounts = {}
        matches, left = 0, 0
        for right in range(len(s2)):
            wdwCounts[s2[right]] = 1 + wdwCounts.get(s2[right], 0)
            if s2[right] in s1Counts:
                if wdwCounts[s2[right]] == s1Counts[s2[right]]:
                    matches += 1
                elif wdwCounts[s2[right]] == s1Counts[s2[right]] + 1:
                    matches -= 1
            
            if matches == len(s1Counts):
                return True
            
            if right - left + 1 < len(s1):
                continue
            
            wdwCounts[s2[left]] -= 1
            if s2[left] in s1Counts:
                if wdwCounts[s2[left]] == s1Counts[s2[left]]:
                    matches += 1
                elif wdwCounts[s2[left]] == s1Counts[s2[left]] - 1:
                    matches -= 1
            
            left += 1
        
        return False