class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while l != r and top != bottom:
            for i in range(l, r):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][r - 1])
            r -= 1

            if not (l != r and top != bottom):
                break

            for i in range(r - 1, l - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][l])
            l += 1
        return result