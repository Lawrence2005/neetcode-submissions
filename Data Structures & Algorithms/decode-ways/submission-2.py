class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        dp[-1] = 1 if s[-1] != '0' else 0
        for i in range(len(s) - 2, -1, -1):
            nextnext = dp[i + 2] if i + 2 < len(s) else 1
            if s[i] == '0':
                dp[i] = 0
            elif s[i] == '1':
                dp[i] = dp[i + 1] + nextnext
            elif s[i] == '2':
                if s[i + 1] <= '6':
                    dp[i] = dp[i + 1] + nextnext
                else:
                    dp[i] = dp[i + 1]
            else:
                dp[i] = dp[i + 1]
        
        return dp[0]
        