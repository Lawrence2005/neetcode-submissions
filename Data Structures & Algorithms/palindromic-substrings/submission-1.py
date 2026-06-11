class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        count = 0
        dp = [False for _ in range(len(s))]
        for i in range(len(s) - 1 , -1, -1):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[j] = dp[j - 1] if j - i > 1 else True
                else:
                    dp[j] = False
                
                if dp[j]:
                    count += 1
        return count