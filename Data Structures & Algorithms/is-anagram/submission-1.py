class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCounts, tCounts = {}, {}
        for i in range(len(s)):
            if s[i] in sCounts:
                sCounts[s[i]] += 1
            else:
                sCounts[s[i]] = 1
            
            if t[i] in tCounts:
                tCounts[t[i]] += 1
            else:
                tCounts[t[i]] = 1
        
        return sCounts == tCounts