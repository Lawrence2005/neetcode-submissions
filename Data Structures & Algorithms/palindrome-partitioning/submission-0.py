class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.helper(s, 0, [])
        return self.result
    
    def helper(self, s, idx, subr):
        if idx >= len(s):
            self.result.append(subr[:])
            return
        
        for i in range(idx, len(s)):
            if self.isPalindrome(s, idx, i):
                subr.append(s[idx: i + 1])
                self.helper(s, i + 1, subr)
                subr.pop()
        
        return
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True