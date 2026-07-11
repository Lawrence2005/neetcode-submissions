class Solution:
    def jump(self, nums: List[int]) -> int:
        currRange, nextRange = 0, 0
        numJumps = 0
        for i in range(len(nums) - 1):
            nextRange = max(nextRange, i + nums[i])
            if i == currRange:
                numJumps += 1
                currRange = nextRange
        return numJumps