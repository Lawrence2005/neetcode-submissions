class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backt(nums, 0, [])
        return self.result
    
    def backt(self, nums, idx, subset):
        if idx == len(nums):
            self.result.append(subset[:])
            return
        
        subset.append(nums[idx])
        self.backt(nums, idx + 1, subset[:])

        subset.pop()
        self.backt(nums, idx + 1, subset[:])
        return