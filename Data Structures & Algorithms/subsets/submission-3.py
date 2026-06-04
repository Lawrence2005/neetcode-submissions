class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(nums, 0, [])
        return self.result
    
    def helper(self, nums, idx, subset):
        if idx == len(nums):
            self.result.append(subset[:])
            return
        
        subset.append(nums[idx])
        self.helper(nums, idx + 1, subset)

        subset.pop()
        self.helper(nums, idx + 1, subset)

        return