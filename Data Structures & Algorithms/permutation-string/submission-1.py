class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Map, windowMap = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            windowMap[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Map[i] == windowMap[i]:
                matches += 1

        left, right = 0, len(s1) - 1
        while right < len(s2) - 1:
            if matches == 26:
                return True

            if windowMap[ord(s2[left]) - ord('a')] == s1Map[ord(s2[left]) - ord('a')]:
                matches -= 1
            windowMap[ord(s2[left]) - ord('a')] -= 1
            if windowMap[ord(s2[left]) - ord('a')] == s1Map[ord(s2[left]) - ord('a')]:
                matches += 1
            
            if windowMap[ord(s2[right + 1]) - ord('a')] == s1Map[ord(s2[right + 1]) - ord('a')]:
                matches -= 1
            windowMap[ord(s2[right + 1]) - ord('a')] += 1
            if windowMap[ord(s2[right + 1]) - ord('a')] == s1Map[ord(s2[right + 1]) - ord('a')]:
                matches += 1
            
            left += 1
            right += 1
        
        return matches == 26
            