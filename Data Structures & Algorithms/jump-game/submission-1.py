class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxRange = 0
        for i in range(len(nums)):
            if i > maxRange:
                return False

            maxRange = max(maxRange, i + nums[i])
        return True
