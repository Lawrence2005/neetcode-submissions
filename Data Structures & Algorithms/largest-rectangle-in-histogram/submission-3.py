class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        largest, stack = 0, []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                lastIdx = stack.pop()
                if stack:
                    largest = max(largest, (i - stack[-1] - 1) * heights[lastIdx])
            stack.append(i)
        return largest