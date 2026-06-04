class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini = ""
        tMap = {}
        for c in t:
            if c in tMap:
                tMap[c] += 1
            else:
                tMap[c] = 1

        left = 0
        windowMap = {l: 0 for l in tMap}
        for right in range(len(s)):
            if s[right] in tMap:
                windowMap[s[right]] += 1
            
            allCover = True
            for l in tMap:
                if windowMap[l] < tMap[l]:
                    allCover = False
                    break
            
            if allCover:
                while left < right:
                    if s[left] in tMap and windowMap[s[left]] - 1 < tMap[s[left]]:
                        break
                    
                    if s[left] in tMap:
                        windowMap[s[left]] -= 1
                    left += 1
                
                if mini == '' or right - left + 1 < len(mini):
                    mini = s[left: right + 1]
            
        return mini