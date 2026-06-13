class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float('-inf')
        currSum = 0
        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSub = max(maxSub, currSum)
        return maxSub