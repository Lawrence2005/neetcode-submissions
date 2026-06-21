class Solution:
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
        
        best = 1
        best = max(best, 1 + self.helper(matrix, (currPos[0] + 1, currPos[1]), matrix[currPos[0]][currPos[1]]))
        best = max(best, 1 + self.helper(matrix, (currPos[0] - 1, currPos[1]), matrix[currPos[0]][currPos[1]]))
        best = max(best, 1 + self.helper(matrix, (currPos[0], currPos[1] + 1), matrix[currPos[0]][currPos[1]]))
        best = max(best, 1 + self.helper(matrix, (currPos[0], currPos[1] - 1), matrix[currPos[0]][currPos[1]]))

        self.dp[currPos] = best
        self.longest = max(self.longest, self.dp[currPos])
        return self.dp[currPos]