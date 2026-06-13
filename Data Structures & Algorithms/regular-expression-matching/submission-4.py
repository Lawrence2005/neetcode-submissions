class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = {}

        return self.helper(s, p, 0, 0)
    
    def helper(self, s, p, sIdx, pIdx):
        if (sIdx, pIdx) in self.dp:
            return self.dp[(sIdx, pIdx)]
        
        if sIdx >= len(s) and pIdx >= len(p):
            return True
        
        if pIdx >= len(p):
            return False
        
        self.dp[(sIdx, pIdx)] = False
        match = sIdx < len(s) and (s[sIdx] == p[pIdx] or p[pIdx] == '.')
        if pIdx + 1 < len(p) and p[pIdx + 1] == '*':
            self.dp[(sIdx, pIdx)] = self.helper(s, p, sIdx, pIdx + 2) or (match and self.helper(s, p, sIdx + 1, pIdx))
        elif match:
            self.dp[(sIdx, pIdx)] = self.helper(s, p, sIdx + 1, pIdx + 1)
        return self.dp[(sIdx, pIdx)]