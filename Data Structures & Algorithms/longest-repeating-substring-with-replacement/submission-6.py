class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        letterCount, maxFreq = {}, 0
        left = 0
        for right in range(len(s)):
            letterCount[s[right]] = 1 + letterCount.get(s[right], 0)
            maxFreq = max(maxFreq, letterCount[s[right]])
            while right - left + 1 - maxFreq > k:
                letterCount[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest