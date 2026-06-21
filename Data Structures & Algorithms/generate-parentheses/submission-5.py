class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper(n, n, [])
        return self.result
    
    def helper(self, numO, numC, subr):
        if numO == 0 and numC == 0:
            self.result.append(''.join(subr))
            return
        
        if numO > 0:
            subr.append('(')
            self.helper(numO - 1, numC, subr)
            subr.pop()

        if numC > numO:
            subr.append(')')
            self.helper(numO, numC - 1, subr)
            subr.pop()
        return