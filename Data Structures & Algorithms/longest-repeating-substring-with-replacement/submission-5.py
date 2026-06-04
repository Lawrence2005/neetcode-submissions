class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        letterCounts, maxFreq = {}, 0
        left = 0
        for right in range(len(s)):
            letterCounts[s[right]] = 1 + letterCounts.get(s[right], 0)
            maxFreq = max(maxFreq, letterCounts[s[right]])

            while right - left + 1 - maxFreq > k:
                letterCounts[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest