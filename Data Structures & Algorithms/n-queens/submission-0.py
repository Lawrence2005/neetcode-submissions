class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.helper(n, set(), set(), set(), [['.' for _ in range(n)] for _ in range(n)], 0)
        return self.result
    
    def helper(self, n, col, posDiag, negDiag, subr, rIdx):
        if rIdx == n:
            self.result.append([''.join(row) for row in subr])
            return
        
        for c in range(n):
            pDiag, nDiag = rIdx + c, rIdx - c
            if c in col or pDiag in posDiag or nDiag in negDiag:
                continue
            
            col.add(c)
            posDiag.add(pDiag)
            negDiag.add(nDiag)
            subr[rIdx][c] = 'Q'
            
            self.helper(n, col, posDiag, negDiag, subr, rIdx + 1)

            col.remove(c)
            posDiag.remove(pDiag)
            negDiag.remove(nDiag)
            subr[rIdx][c] = '.'
        
        return
