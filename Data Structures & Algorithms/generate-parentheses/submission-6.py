class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper(n, 0, 0, [])
        return self.result
    
    def helper(self, n, numO, numC, subr):
        if numO == n and numC == n:
            self.result.append(''.join(subr))
            return
        
        if numO < n:
            subr.append('(')
            self.helper(n, numO + 1, numC, subr)
            subr.pop()
        
        if numC < numO:
            subr.append(')')
            self.helper(n, numO, numC + 1, subr)
            subr.pop()
            
        return