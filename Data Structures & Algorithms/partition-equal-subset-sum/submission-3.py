class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        halfSum = sum(nums) // 2
        dp = [0 for _ in range(halfSum + 1)]
        for n in nums:
            for i in range(halfSum, n - 1, -1):
                dp[i] = max(dp[i], dp[i - n] + n)
        return dp[-1] == halfSum
        