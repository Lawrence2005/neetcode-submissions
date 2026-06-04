# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        tail = head
        for _ in range((length - 1) // 2):
            tail = tail.next

        tmp = tail.next
        tail.next = None
        tail = tmp

        tail = self.revList(tail)

        curr = head
        while curr and tail:
            tmpC, tmpT = curr.next, tail.next

            curr.next = tail
            tail.next = tmpC

            curr = tmpC
            tail = tmpT

    def revList(self, head) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = self.revList(head.next)

        head.next.next = head
        head.next = None
        
        return newHead