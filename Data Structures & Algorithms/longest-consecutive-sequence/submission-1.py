class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        numsSet = set(nums)
        for n in nums:
            left, right = n - 1, n + 1
            if left in numsSet:
                continue
            
            currLen = 1
            while right in numsSet:
                currLen += 1
                right += 1
            
            result = max(result, currLen)
            
        return result