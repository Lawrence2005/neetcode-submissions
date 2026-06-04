class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Map = {}
        for c in s1:
            s1Map[c] = 1 + s1Map.get(c, 0)
        
        wdwMap, covers = {}, 0
        left = 0
        for right in range(len(s2)):
            wdwMap[s2[right]] = 1 + wdwMap.get(s2[right], 0)
            if s2[right] in s1Map:
                if wdwMap[s2[right]] == s1Map[s2[right]]:
                    covers += 1
                elif wdwMap[s2[right]] == s1Map[s2[right]] + 1:
                    covers -= 1

            if covers == len(s1Map):
                return True

            if right - left + 1 < len(s1):
                continue

            wdwMap[s2[left]] -= 1
            if s2[left] in s1Map:
                if wdwMap[s2[left]] == s1Map[s2[left]]:
                    covers += 1
                elif wdwMap[s2[left]] == s1Map[s2[left]] - 1:
                    covers -= 1

            left += 1
            
        return False