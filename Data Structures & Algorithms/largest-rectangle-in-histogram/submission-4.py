class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        heights = [0] + heights + [0]
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                lastIdx = stack.pop()
                if stack:
                    largest = max(largest, (i - stack[-1] - 1) * heights[lastIdx])
            stack.append(i)
        return largest