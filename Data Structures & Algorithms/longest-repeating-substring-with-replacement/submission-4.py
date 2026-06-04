class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts, maxFreq = {}, 0
        left = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            maxFreq = max(maxFreq, counts[s[right]])

            while right - left + 1 - maxFreq > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest