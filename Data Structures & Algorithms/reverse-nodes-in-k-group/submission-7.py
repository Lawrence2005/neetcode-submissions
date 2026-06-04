# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head or not head.next:
            return head
        
        result = None
        prevT = None
        slow, fast = head, head
        while fast:
            for _ in range(k - 1):
                fast = fast.next
                if not fast:
                    return result if result else head
            
            result = fast if not result else result

            if prevT:
                prevT.next = fast
            
            newSlow = fast.next

            prev, curr = newSlow, slow
            while curr != newSlow:
                tmp = curr.next
                curr.next = prev
                prev = curr

                curr = tmp
            
            prevT = slow
            slow, fast = newSlow, newSlow
        
        return result