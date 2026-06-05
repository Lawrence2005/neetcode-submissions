class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.paliTable = self.getPali(s)

        self.result = []
        self.helper(s, [], 0)
        return self.result
    
    def helper(self, s, subr, idx):
        if idx == len(s):
            self.result.append(subr[:])
            return
        
        for i in range(idx, len(s)):
            if not self.paliTable[idx][i]:
                continue

            subr.append(s[idx: i + 1])
            self.helper(s, subr, i + 1)
            subr.pop()
            
        return

    def getPali(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s), -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if j - i > 1 else True
        
        return dp