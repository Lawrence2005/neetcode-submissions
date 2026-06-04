class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        frontProd, backProd = [], []
        curr = 1
        for i in range(len(nums)):
            frontProd.append(curr)
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            backProd.append(curr)
            curr *= nums[i]
        for i in range(len(nums) // 2):
            temp = backProd[i]
            backProd[i] = backProd[len(nums) - 1 - i]
            backProd[len(nums) - 1 - i] = temp
        
        output = []
        for i in range(len(nums)):
            output.append(frontProd[i] * backProd[i])
        return output