class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {n}
        curr = n
        while curr != 1:
            currSum = 0
            while curr > 0:
                digit = curr % 10
                currSum += digit ** 2
                curr //= 10
            
            if currSum in nums:
                return False
            
            nums.add(currSum)
            curr = currSum
        return True