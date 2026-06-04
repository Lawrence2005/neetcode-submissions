class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        array = [[] for _ in range(len(nums) + 1)]
        for n in count:
            array[count[n]].append(n)
        
        result, count = [], 0
        for i in range(len(nums), -1, -1):
            result += array[i]
            count += len(array[i])
            if count == k:
                break

        return result