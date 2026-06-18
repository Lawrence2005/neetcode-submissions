class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[0]) - 1 - j]
                matrix[i][len(matrix[0]) - 1 - j] = tmp
        return