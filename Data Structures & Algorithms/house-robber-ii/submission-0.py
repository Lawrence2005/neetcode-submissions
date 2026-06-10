class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1, dp2 = [nums[0], max(nums[0], nums[1])], [nums[1], max(nums[1], nums[2])]
        for i in range(2, len(nums) - 1):
            dp1.append(max(nums[i] + dp1[i - 2], dp1[i - 1]))
            dp2.append(max(nums[i + 1] + dp2[i - 2], dp2[i - 1]))
        
        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])
