class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numsSum = sum(nums)
        if abs(target) > numsSum:
            return 0
        
        if (numsSum + target) % 2 != 0:
            return 0
        
        subSum = (numsSum + target) // 2
        dp = [0 for _ in range(subSum + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(subSum, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[-1]