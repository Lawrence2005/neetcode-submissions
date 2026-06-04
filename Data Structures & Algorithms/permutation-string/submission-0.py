class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map, windowMap = {}, {}
        for i in range(len(s1)):
            if s1[i] in s1Map:
                s1Map[s1[i]] += 1
            else:
                s1Map[s1[i]] = 1

            if s2[i] in windowMap:
                windowMap[s2[i]] += 1
            else:
                windowMap[s2[i]] = 1

        left, right = 0, len(s1) - 1
        while right < len(s2):
            if windowMap == s1Map:
                return True
            
            if right == len(s2) - 1:
                break

            windowMap[s2[left]] -= 1
            if windowMap[s2[left]] == 0:
                del windowMap[s2[left]]

            if s2[right + 1] in windowMap:
                windowMap[s2[right + 1]] += 1
            else:
                windowMap[s2[right + 1]] = 1

            left += 1
            right += 1
        
        return False
            
            

