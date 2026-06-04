class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minNum = nums[left + (right - left) // 2]
        while left <= right:
            if nums[left] < nums[right]:
                minNum = min(minNum, nums[left])
                break

            mid = left + (right - left) // 2
            minNum = min(minNum, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minNum