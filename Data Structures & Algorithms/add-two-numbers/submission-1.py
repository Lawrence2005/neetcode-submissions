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

        carry = 0
        currL1, currL2 = l1, l2
        while currL1 or currL2 or carry:
            l1Val = currL1.val if currL1 else 0
            l2Val = currL2.val if currL2 else 0
            
            dSum = l1Val + l2Val + carry

            currNext = ListNode(dSum % 10)
            curr.next = currNext
            curr = curr.next

            carry = dSum // 10

            currL1 = currL1.next if currL1 else None
            currL2 = currL2.next if currL2 else None

        return dummy.next