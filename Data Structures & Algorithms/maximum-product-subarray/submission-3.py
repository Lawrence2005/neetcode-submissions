class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        maxP, minP = 1, 1
        for n in nums:
            if n == 0:
                maxP, minP = 1, 1
                continue

            tmp = maxP
            maxP = max(maxP * n, minP * n, n)
            minP = min(minP * n, tmp * n, n)
            ans = max(ans, maxP)
        return ans