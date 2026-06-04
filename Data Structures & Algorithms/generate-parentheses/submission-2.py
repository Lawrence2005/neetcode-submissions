class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper(n, [], 0, 0)
        return self.result
    
    def helper(self, n, subr, numO, numC):
        if numO == n and numC == n:
            self.result.append(''.join(subr))
            return
        
        if numO == numC:
            subr.append('(')
            self.helper(n, subr, numO + 1, numC)
            subr.pop()
        elif numO > numC:
            if numO != n:
                subr.append('(')
                self.helper(n, subr, numO + 1, numC)
                subr.pop()
            
            subr.append(')')
            self.helper(n, subr, numO, numC + 1)
            subr.pop()
        
        return