class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        left = 0
        windowFreq = {}
        for right in range(len(s)):
            if s[right] in windowFreq:
                windowFreq[s[right]] += 1
            else:
                windowFreq[s[right]] = 1
            
            if right - left + 1 - max(windowFreq.values()) <= k:
                longest = max(longest, right - left + 1)
            else:
                while right - left + 1 - max(windowFreq.values()) > k:
                    windowFreq[s[left]] -= 1
                    left += 1
        
        return longest