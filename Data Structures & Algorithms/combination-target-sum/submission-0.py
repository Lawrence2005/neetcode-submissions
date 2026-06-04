class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.helper(nums, target, 0, [], 0)
        return self.result
    
    def helper(self, nums, target, idx, subset, currSum):
        if currSum >= target or idx == len(nums):
            if currSum == target:
                self.result.append(subset[:])
            return
        
        subset.append(nums[idx])
        currSum += nums[idx]
        self.helper(nums, target, idx, subset, currSum)

        subset.pop()
        currSum -= nums[idx]
        self.helper(nums, target, idx + 1, subset, currSum)

        return