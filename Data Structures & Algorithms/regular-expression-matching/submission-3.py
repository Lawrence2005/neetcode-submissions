class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = {}

        return self.helper(s, p, 0, 0)

    def helper(self, s, p, l, r):
        if (l, r) in self.dp:
            return self.dp[(l, r)]
        
        if l >= len(s) and r >= len(p):
            return True
        
        if r >= len(p):
            return False
        
        match = l < len(s) and (s[l] == p[r] or p[r] == '.')
        if r + 1 < len(p) and p[r + 1] == '*':
            self.dp[(l, r)] = self.helper(s, p, l, r + 2) or (match and self.helper(s, p, l + 1, r))
            return self.dp[(l, r)]
        
        if match:
            self.dp[(l, r)] = self.helper(s, p, l + 1, r + 1)
            return self.dp[(l, r)]
        
        self.dp[(l, r)] = False
        return self.dp[(l, r)]