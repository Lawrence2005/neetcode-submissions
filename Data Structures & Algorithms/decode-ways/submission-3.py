class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1 if s[-1] != '0' else 0

        curr = 1 if s[-1] != '0' else 0
        prev = 1
        for i in range(len(s) - 2, -1, -1):
            tmp = curr
            if s[i] == '0':
                curr = 0
            elif s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                curr += prev
            prev = tmp
        return curr