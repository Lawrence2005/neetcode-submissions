class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(nums, [])
        return self.result
    
    def helper(self, nums, p):
        if len(nums) == 0:
            self.result.append(p[:])
            return
        
        for i in range(len(nums)):
            p.append(nums[i])
            self.helper(nums[: i] + nums[i + 1:], p)
            p.pop()
        
        return
        