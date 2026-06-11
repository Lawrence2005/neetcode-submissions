class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ("", 0)
        dp = [False for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, i - 1, -1):
                if s[j] == s[i]:
                    dp[j] = dp[j - 1] if j - i > 1 else True
                else:
                    dp[j] = False
                
                if not dp[j] or j - i + 1 <= ans[1]:
                    continue
                
                ans = (s[i: j + 1], j - i + 1)
        return ans[0]