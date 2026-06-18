class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.longest = 1
        self.dp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.helper(matrix, (i, j), float('-inf'))
        return self.longest
    
    def helper(self, matrix, currPos, prevVal):
        if not (0 <= currPos[0] < len(matrix) and 0 <= currPos[1] < len(matrix[0])):
            return 0
        
        if matrix[currPos[0]][currPos[1]] <= prevVal:
            return 0
        
        if currPos in self.dp:
            return self.dp[currPos]
        
        longest = 1
        longest = max(longest, 1 + self.helper(matrix, (currPos[0] + 1, currPos[1]), matrix[currPos[0]][currPos[1]]))
        longest = max(longest, 1 + self.helper(matrix, (currPos[0] - 1, currPos[1]), matrix[currPos[0]][currPos[1]]))
        longest = max(longest, 1 + self.helper(matrix, (currPos[0], currPos[1] + 1), matrix[currPos[0]][currPos[1]]))
        longest = max(longest, 1 + self.helper(matrix, (currPos[0], currPos[1] - 1), matrix[currPos[0]][currPos[1]]))
        
        self.dp[currPos] = longest
        self.longest = max(self.longest, longest)
        return longest