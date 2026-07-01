class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, set(), (i, j), 0):
                    return True
        return False
    
    def helper(self, board, word, visited, currPos, currIdx):
        if board[currPos[0]][currPos[1]] != word[currIdx]:
            return False
        
        if currIdx == len(word) - 1:
            return True
        
        visited.add(currPos)
        for d in self.DIRECTIONS:
            neighbor = (currPos[0] + d[0], currPos[1] + d[1])
            if not (0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0])) or neighbor in visited:
                continue
            
            if self.helper(board, word, visited, neighbor, currIdx + 1):
                return True
            
        visited.remove(currPos)
        return False