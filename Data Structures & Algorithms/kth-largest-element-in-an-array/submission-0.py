class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-nums[i] for i in range(len(nums))]
        heapq.heapify(heap)

        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)