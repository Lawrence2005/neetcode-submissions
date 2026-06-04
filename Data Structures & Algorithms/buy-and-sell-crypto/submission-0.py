class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy, sold = -prices[0], 0
        for i in range(1, len(prices)):
            sold = buy + prices[i]
            buy = max(buy, -prices[i])
            maxProfit = max(maxProfit, sold)

        return maxProfit