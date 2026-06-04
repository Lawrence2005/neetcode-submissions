class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if self.canFinish(piles, mid, h):
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        return k
    
    def canFinish(self, piles, k, h):
        time = 0
        for p in piles:
            time += (p + k - 1) // k

        return time <= h 