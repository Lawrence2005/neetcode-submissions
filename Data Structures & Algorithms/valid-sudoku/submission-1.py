class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                rows[i][int(board[i][j]) - 1] += 1
                cols[j][int(board[i][j]) - 1] += 1
                boxes[i // 3 * 3 + j // 3][int(board[i][j]) - 1] += 1

                if rows[i][int(board[i][j]) - 1] > 1 or cols[j][int(board[i][j]) - 1] > 1 or boxes[i // 3 * 3 + j // 3][int(board[i][j]) - 1] > 1:
                    return False
        
        return True