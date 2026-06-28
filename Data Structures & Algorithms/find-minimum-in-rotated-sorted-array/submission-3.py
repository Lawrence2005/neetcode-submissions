class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return min(mini, nums[left])
            
            mid = left + (right - left) // 2
            mini = min(mini, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return mini