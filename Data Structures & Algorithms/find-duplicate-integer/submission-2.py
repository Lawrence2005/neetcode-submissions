class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow == fast == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        resIdx = 0
        while resIdx != slow:
            slow = nums[slow]
            resIdx = nums[resIdx]
        
        return resIdx