class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        currMax, nextMax = 0, 0
        for i in range(len(nums) - 1):
            nextMax = max(nextMax, i + nums[i])
            if i == currMax:
                currMax = nextMax
                count += 1
        return count