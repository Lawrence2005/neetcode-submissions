class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if j - i > 1 else True
                if dp[i][j]:
                    count += 1
        return count