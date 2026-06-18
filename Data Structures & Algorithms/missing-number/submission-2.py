class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for n in nums:
            missing ^= n
        for n in range(len(nums) + 1):
            missing ^= n
        return missing