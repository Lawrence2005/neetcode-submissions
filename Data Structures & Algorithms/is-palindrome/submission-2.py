class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ""
        for c in s:
            if c.isalnum():
                processed += c.lower()
        
        left, right = 0, len(processed) - 1
        while left < right:
            if processed[left] != processed[right]:
                return False

            left += 1
            right -= 1

        return True