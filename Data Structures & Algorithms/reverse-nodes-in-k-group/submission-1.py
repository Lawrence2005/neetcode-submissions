# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        
        newHead = None
        lastLast = None
        slow, fast = head, head
        while fast:
            for i in range(k -1):
                fast = fast.next
                if not fast:
                    return newHead
            
            newHead = fast if not newHead else newHead

            newSlow = fast.next
            prev, curr = newSlow, slow
            while curr != newSlow:
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp
            if lastLast:
                lastLast.next = fast
            
            lastLast = slow
            slow = newSlow
            fast = slow
        
        return newHead