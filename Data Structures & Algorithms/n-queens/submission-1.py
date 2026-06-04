class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.helper(n, set(), set(), set(), [['.' for _ in range(n)] for _ in range(n)], 0)
        return self.result
    
    def helper(self, n, cols, pDiags, nDiags, subr, rIdx):
        if rIdx == n:
            self.result.append([''.join(row) for row in subr])
            return
        
        for c in range(n):
            pDiag, nDiag = rIdx + c, rIdx - c
            if c in cols or pDiag in pDiags or nDiag in nDiags:
                continue
            
            cols.add(c)
            pDiags.add(pDiag)
            nDiags.add(nDiag)
            subr[rIdx][c] = 'Q'

            self.helper(n, cols, pDiags, nDiags, subr, rIdx + 1)

            cols.remove(c)
            pDiags.remove(pDiag)
            nDiags.remove(nDiag)
            subr[rIdx][c] = '.'
        
        return