class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper(n, 0, 0, [])
        return self.result
    
    def helper(self, n, oCount, cCount, subr):
        if oCount == n and cCount == n:
            self.result.append(''.join(subr))
            return
        
        if oCount < n:
            subr.append('(')
            self.helper(n, oCount + 1, cCount, subr)
            subr.pop()
        
        if cCount < oCount:
            subr.append(')')
            self.helper(n, oCount, cCount + 1, subr)
            subr.pop()
        return