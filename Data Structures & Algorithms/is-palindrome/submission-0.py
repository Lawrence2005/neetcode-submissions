class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ""
        for i in range(len(s)):
            if s[i].isalnum():
                if s[i].isalpha():
                    processed += s[i].lower()
                else:
                    processed += s[i]

        for i in range(len(processed) // 2):
            if processed[i] != processed[len(processed) - 1 - i]:
                return False
            
        return True