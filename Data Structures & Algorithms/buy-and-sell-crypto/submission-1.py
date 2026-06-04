class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sold = -prices[0], 0
        for i in range(1, len(prices)):
            sold = max(sold, buy + prices[i])
            buy = max(buy, -prices[i])

        return sold