class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        heights = [0] + heights + [0]
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                lastIndex = stack.pop()
                if stack:
                    maxArea = max(maxArea, heights[lastIndex] * (i - stack[-1] - 1))
            stack.append(i)
        return maxArea
