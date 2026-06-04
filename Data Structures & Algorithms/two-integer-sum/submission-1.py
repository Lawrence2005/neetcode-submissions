class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        indice1, indice2 = -1, -1
        for i in range(len(nums)):
            want = target - nums[i]
            if want in track:
                return [track[want], i]
            
            track[nums[i]] = i
        
        return [indice1, indice2]

            