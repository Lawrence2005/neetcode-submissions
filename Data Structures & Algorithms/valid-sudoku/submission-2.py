class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False for _ in range(9)] for _ in range(9)]
        col = [[False for _ in range(9)] for _ in range(9)]
        box = [[False for _ in range(9)] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                boxIdx = i // 3 * 3 + j // 3
                if row[i][int(board[i][j]) - 1] or col[j][int(board[i][j]) - 1] or box[boxIdx][int(board[i][j]) - 1]:
                    return False
                
                row[i][int(board[i][j]) - 1] = True
                col[j][int(board[i][j]) - 1] = True
                box[boxIdx][int(board[i][j]) - 1] = True
        return True