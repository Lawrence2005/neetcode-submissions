class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstR0, firstC0 = False, False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstR0 = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstC0 = True
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in range(len(matrix[0]))]
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        
        if firstR0:
            matrix[0] = [0 for _ in range(len(matrix[0]))]
        if firstC0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return