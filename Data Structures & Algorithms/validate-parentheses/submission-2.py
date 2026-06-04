class Solution:
    def isValid(self, s: str) -> bool:
        pairings = {')': '(',
                    '}': '{',
                    ']': '['}

        stack = []
        for c in s:
            if c not in pairings:
                stack.append(c)
            else:
                if not stack or stack[-1] != pairings[c]:
                    return False
                
                stack.pop()
        
        return not stack