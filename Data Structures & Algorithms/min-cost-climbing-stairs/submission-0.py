class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:]
        for i in range(len(cost) - 3, -1, -1):
            dp[i] += min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])