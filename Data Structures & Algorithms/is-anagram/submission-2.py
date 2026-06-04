class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0 for _ in range(26)]
        for i in range(len(s)):
            s_index, t_index = ord(s[i]) - ord('a'), ord(t[i]) - ord('a')
            counts[s_index] += 1
            counts[t_index] -= 1
        
        for i in range(26):
            if counts[i] != 0:
                return False
        
        return True