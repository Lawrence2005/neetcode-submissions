class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                break
            
            if currSum < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]