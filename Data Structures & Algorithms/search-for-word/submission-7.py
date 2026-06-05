class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, (i, j), visited, word, 0):
                    return True
        
        return False
    
    def helper(self, board, currPos, visited, word, idx):
        if board[currPos[0]][currPos[1]] != word[idx]:
            return False
        
        if idx == len(word) - 1:
            return True
        
        visited[currPos[0]][currPos[1]] = True
        for d in self.DIRECTIONS:
            neighbor = (currPos[0] + d[0], currPos[1] + d[1])
            if not (0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0])) or visited[neighbor[0]][neighbor[1]]:
                continue

            if self.helper(board, neighbor, visited, word, idx + 1):
                return True
        
        visited[currPos[0]][currPos[1]] = False
        return False