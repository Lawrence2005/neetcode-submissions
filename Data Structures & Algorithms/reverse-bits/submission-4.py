class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            digit = (n >> i) & 1
            result |= digit << (31 - i)
        return result