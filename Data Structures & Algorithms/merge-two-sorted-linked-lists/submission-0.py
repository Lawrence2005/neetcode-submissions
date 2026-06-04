# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1 or not list2:
            return list1 or list2
        
        dummy = ListNode()
        curr = dummy
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                if l1:
                    curr.next.next = None
            else:
                curr.next = l2
                l2 = l2.next
                if l2:
                    curr.next.next = None
            curr = curr.next
        
        if not l1:
            curr.next = l2
        else:
            curr.next = l1
        
        return dummy.next