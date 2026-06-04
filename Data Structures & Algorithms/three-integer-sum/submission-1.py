class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            if nums[i] > 0:
                break
            
            want = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum < want:
                    left += 1
                elif currSum > want:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
        
        return result
