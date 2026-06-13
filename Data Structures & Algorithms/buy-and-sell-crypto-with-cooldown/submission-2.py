class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0, -prices[0], 0]
        for i in range(1, len(prices)):
            tmp = dp[:]
            dp[0] = max(tmp[0], tmp[2])
            dp[1] = max(tmp[0] - prices[i], tmp[1])
            dp[2] = tmp[1] + prices[i]
        return max(dp[0], dp[2])