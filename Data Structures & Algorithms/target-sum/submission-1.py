class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numsSum = sum(nums)
        if abs(target) > numsSum:
            return 0
        
        if (numsSum + target) % 2 != 0:
            return 0
        
        posTarget = (numsSum + target) // 2
        dp = [0 for _ in range(posTarget + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(posTarget, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[-1]