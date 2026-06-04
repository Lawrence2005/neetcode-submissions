# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = self.revList(slow.next)
        slow.next = None

        head = self.mergeLists(head, tail)
    
    def revList(self, head):
        if not head or not head.next:
            return head
        
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            
            curr = tmp
        
        return prev
    
    def mergeLists(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2
        
        dummy = ListNode()
        curr = dummy
        
        h1, h2 = head1, head2
        while h1 and h2:
            curr.next = h1
            h1 = h1.next
            curr = curr.next

            curr.next = h2
            h2 = h2.next
            curr = curr.next
        
        curr.next = h1 if h1 else h2

        return dummy.next