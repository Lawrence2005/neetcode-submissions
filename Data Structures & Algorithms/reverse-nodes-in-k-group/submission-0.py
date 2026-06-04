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
        prevT, currH = None, head
        while currH:
            fast = currH
            for _ in range(k - 1):
                if not fast.next:
                    return result if result else head
                
                fast = fast.next

            nextH = fast.next

            newH, newT = self.revList(currH, fast)
            if currH == head:
                result = newH

            if prevT:
                prevT.next = newH

            newT.next = nextH

            prevT, currH = newT, nextH

        return result
            
    def revList(self, head, tail):
        if not head or not head.next:
            return head
        
        stop = tail.next
        prev, curr = None, head
        while curr != stop:
            tmp = curr.next
            curr.next = prev
            prev = curr

            curr = tmp
        
        return tail, head
