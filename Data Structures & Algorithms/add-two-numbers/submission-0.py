# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        
        dummy = ListNode()
        curr = dummy

        currL1, currL2 = l1, l2
        carry = 0
        while currL1 and currL2:
            dSum = currL1.val + currL2.val + carry
            carry = 1 if dSum >= 10 else 0

            currNext = ListNode(dSum % 10)
            curr.next = currNext
            curr = curr.next

            currL1, currL2 = currL1.next, currL2.next
        
        remain = currL1 if currL1 else currL2
        while remain:
            dSum = remain.val + carry
            carry = 1 if dSum >= 10 else 0

            currNext = ListNode(dSum % 10)
            curr.next = currNext
            curr = curr.next

            remain = remain.next
        
        if carry:
            tail = ListNode(1)
            curr.next = tail
        
        return dummy.next