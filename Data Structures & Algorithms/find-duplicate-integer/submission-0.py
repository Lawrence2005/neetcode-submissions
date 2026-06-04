class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow == fast == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        newPos = 0
        while newPos != slow:
            newPos = nums[newPos]
            slow = nums[slow]

        return newPos