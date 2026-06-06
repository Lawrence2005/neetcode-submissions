class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.markZ(board, (i, 0))
            if board[i][-1] == 'O':
                self.markZ(board, (i, len(board[0]) - 1))
        
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.markZ(board, (0, i))
            if board[-1][i] == 'O':
                self.markZ(board, (len(board) - 1, i))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'
        return

    def markZ(self, board, currPos):
        board[currPos[0]][currPos[1]] = 'Z'
        for d in self.DIRECTIONS:
            neighbor = (currPos[0] + d[0], currPos[1] + d[1])
            if not (0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0])) or board[neighbor[0]][neighbor[1]] != 'O':
                continue
            
            self.markZ(board, neighbor)
        return