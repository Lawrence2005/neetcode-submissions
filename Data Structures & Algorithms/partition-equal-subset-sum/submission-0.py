class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2 != 0:
            return False
        
        halfSum = numsSum // 2
        dp = [0 for _ in range(halfSum + 1)]
        for n in nums:
            for i in range(halfSum, n - 1, -1):
                dp[i] = max(dp[i], dp[i - n] + n)
        return True if dp[-1] == halfSum else False
