class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    continue
                
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    rowZero = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    for k in range(len(matrix)):
                        matrix[k][j] = 0
                if matrix[i][0] == 0:
                    matrix[i] = [0 for _ in range(len(matrix[0]))]
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if rowZero:
            matrix[0] = [0 for _ in range(len(matrix[0]))]
        return