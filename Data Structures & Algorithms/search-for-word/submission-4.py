class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, 0, (i, j), visited):
                    return True
        
        return False

    def helper(self, board, word, idx, currPos, visited):
        if board[currPos[0]][currPos[1]] != word[idx]:
            return False
        
        if idx == len(word) - 1:
            return True
        
        visited[currPos[0]][currPos[1]] = True
        for d in self.DIRECTIONS:
            neighbor = (currPos[0] + d[0], currPos[1] + d[1])
            if not (0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0])) or visited[neighbor[0]][neighbor[1]]:
                continue
            
            if self.helper(board, word, idx + 1, neighbor, visited):
                return True
        
        visited[currPos[0]][currPos[1]] = False

        return False