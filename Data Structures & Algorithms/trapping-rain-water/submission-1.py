class Solution:
    def trap(self, height: List[int]) -> int:
        trap = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom  = stack.pop()
                if stack:
                    trap += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[bottom])

            stack.append(i)

        return trap