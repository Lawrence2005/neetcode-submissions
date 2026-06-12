class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dp[-1][-1] = True
        for i in range(len(s1) - 1, -1, -1):
            dp[len(s2)][i] = dp[len(s2)][i + 1] if s1[i] == s3[len(s2) + i] else False
        for i in range(len(s2) - 1, -1, -1):
            dp[i][len(s1)] = dp[i + 1][len(s1)] if s2[i] == s3[len(s1) + i] else False
        
        for i in range(len(s2) - 1, -1, -1):
            for j in range(len(s1) - 1, -1, -1):
                if s1[j] != s3[i + j] and s2[i] != s3[i + j]:
                    dp[i][j] = False
                elif s1[j] == s3[i + j] and s2[i] == s3[i + j]:
                    dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                elif s1[j] == s3[i + j]:
                    dp[i][j] = dp[i][j + 1]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]