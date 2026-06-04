class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        mini = ""
        tMap = {}
        for c in t:
            if c in tMap:
                tMap[c] += 1
            else:
                tMap[c] = 1

        windowMap = {l: 0 for l in tMap}

        left, covers = 0, 0
        for right in range(len(s)):
            if s[right] in tMap:
                windowMap[s[right]] += 1
                if windowMap[s[right]] == tMap[s[right]]:
                    covers += 1
            
            if covers == len(tMap):
                while left < right:
                    if s[left] in tMap and windowMap[s[left]] - 1 < tMap[s[left]]:
                        break
                    
                    if s[left] in tMap:
                        windowMap[s[left]] -= 1
                    left += 1
                
                if mini == '' or right - left + 1 < len(mini):
                    mini = s[left: right + 1]
            
        return mini