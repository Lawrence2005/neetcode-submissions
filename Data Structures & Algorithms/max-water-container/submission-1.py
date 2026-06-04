class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        left, right = 0, len(heights) - 1
        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea