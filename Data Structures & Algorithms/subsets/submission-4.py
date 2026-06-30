class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(nums, [], 0)
        return self.result
    
    def helper(self, nums, subr, idx):
        if idx == len(nums):
            self.result.append(subr[:])
            return
        
        subr.append(nums[idx])
        self.helper(nums, subr, idx + 1)
        subr.pop()

        self.helper(nums, subr, idx + 1)
        return