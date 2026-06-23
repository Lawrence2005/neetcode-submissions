class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow == fast == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        res = 0
        while res != slow:
            res = nums[res]
            slow = nums[slow]
        return res