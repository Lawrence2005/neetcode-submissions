class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.helper(n, set(), set(), set(), [['.' for _ in range(n)] for _ in range(n)], 0)
        return self.result
    
    def helper(self, n, cols, pDiags, nDiags, subr, r):
        if r == n:
            self.result.append([''.join(row) for row in subr])
            return
        
        for c in range(n):
            pDiag, nDiag = r + c, r - c
            if c in cols or pDiag in pDiags or nDiag in nDiags:
                continue
            
            subr[r][c] = 'Q'
            cols.add(c)
            pDiags.add(pDiag)
            nDiags.add(nDiag)

            self.helper(n, cols, pDiags, nDiags, subr, r + 1)

            subr[r][c] = '.'
            cols.remove(c)
            pDiags.remove(pDiag)
            nDiags.remove(nDiag)
        
        return