class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tCounts = {}
        for c in t:
            tCounts[c] = 1 + tCounts.get(c, 0)
        
        result, wdwCounts = None, {}
        covers, left = 0, 0
        for right in range(len(s)):
            if s[right] not in tCounts:
                continue
            
            wdwCounts[s[right]] = 1 + wdwCounts.get(s[right], 0)
            if wdwCounts[s[right]] == tCounts[s[right]]:
                covers += 1
            
            if covers < len(tCounts):
                continue
            
            while left <= right:
                if s[left] in tCounts and wdwCounts[s[left]] == tCounts[s[left]]:
                    break
                
                if s[left] in tCounts: # wdwCounts[s[left]] > tCounts[s[left]]
                    wdwCounts[s[left]] -= 1

                left += 1

            if not result or right - left + 1 < len(result):
                result = s[left: right + 1]
        
        return result if result else ""