class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curr = 0
        for n in nums:
            curr += n
            maxSum = max(maxSum, curr)
            curr = max(curr, 0)
        return maxSum