class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.helper(nums, 0, [])
        return self.result
    
    def helper(self, nums, idx, subset):
        if idx >= len(nums):
            self.result.append(subset[:])
            return
        
        subset.append(nums[idx])
        self.helper(nums, idx + 1, subset)

        subset.pop()
        nextIdx = idx + 1
        while nextIdx < len(nums) and nums[nextIdx] == nums[idx]:
            nextIdx += 1
        self.helper(nums, nextIdx, subset)

        return