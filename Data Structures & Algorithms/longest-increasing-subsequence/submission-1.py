class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = 1
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            longest = max(longest, dp[i])
        return longest