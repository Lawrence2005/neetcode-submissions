class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        last_index = {}
        left = 0
        for right in range(len(s)):
            if s[right] in last_index and last_index[s[right]] >= left:
                left = last_index[s[right]] + 1
            last_index[s[right]] = right
    
            longest = max(longest, right - left + 1)
        
        return longest