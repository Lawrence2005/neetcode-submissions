class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        last_index = {}
        left = 0
        for i in range(len(s)):
            if s[i] in last_index and last_index[s[i]] >= left:
                left = last_index[s[i]] + 1
            else:
                longest = max(longest, i - left + 1)
            last_index[s[i]] = i
        
        return longest