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

        self.mergeLists(head, tail)

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
            return
        
        h1, h2 = head1, head2
        while h1 and h2:
            h1Next, h2Next = h1.next, h2.next

            h1.next = h2
            h2.next = h1Next

            h1, h2 = h1Next, h2Next
        
        return