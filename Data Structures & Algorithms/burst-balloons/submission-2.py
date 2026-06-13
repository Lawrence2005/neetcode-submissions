class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.dp = {}
        nums = [1] + nums + [1]
        
        return self.helper(nums, 1, len(nums) - 2)
    
    def helper(self, nums, l, r):
        if (l, r) in self.dp:
            return self.dp[(l, r)]
        
        if l > r:
            return 0
        
        self.dp[(l, r)] = 0
        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += self.helper(nums, l, i - 1) + self.helper(nums, i + 1, r)
            self.dp[(l, r)] = max(self.dp[(l, r)], coins)

        return self.dp[(l, r)]