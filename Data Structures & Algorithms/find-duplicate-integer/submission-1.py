class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow == fast == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        resPos = 0
        while resPos != slow:
            resPos = nums[resPos]
            slow = nums[slow]
        
        return resPos