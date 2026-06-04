class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stones[i] for i in range(len(stones))]
        heapq.heapify(heap)

        while heap and len(heap) > 1:
            largest, secLargest = heapq.heappop(heap), heapq.heappop(heap)
            if largest != secLargest:
                heapq.heappush(heap, largest - secLargest)
        
        return -heap[0] if heap else 0