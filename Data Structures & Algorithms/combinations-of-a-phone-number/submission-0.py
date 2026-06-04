class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        self.dMap = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}
        self.result = []
        self.helper(digits, 0, [])
        return self.result
    
    def helper(self, digits, idx, subr):
        if idx == len(digits):
            self.result.append(''.join(subr))
            return
        
        for char in self.dMap[digits[idx]]:
            subr.append(char)
            self.helper(digits, idx + 1, subr)
            subr.pop()
        
        return