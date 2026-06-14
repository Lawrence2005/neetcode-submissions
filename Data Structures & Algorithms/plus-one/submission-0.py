class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits[:]
        currIdx = len(result) - 1
        while currIdx >= 0:
            result[currIdx] += 1
            if result[currIdx] < 10:
                return result

            result[currIdx] = 0
            currIdx -= 1
        result = [1] + result

        return result