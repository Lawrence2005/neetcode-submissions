class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = minP = ans = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], maxP * nums[i], minP * nums[i])
            maxP = max(candidates)
            minP = min(candidates)
            ans = max(ans, maxP)
        return ans