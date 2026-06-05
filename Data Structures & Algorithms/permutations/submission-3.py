class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(nums, [])
        return self.result
    
    def helper(self, nums, subr):
        if len(nums) == 0:
            self.result.append(subr[:])
            return
        
        for i in range(len(nums)):
            subr.append(nums[i])
            self.helper(nums[:i] + nums[i + 1:], subr)
            subr.pop()
        
        return