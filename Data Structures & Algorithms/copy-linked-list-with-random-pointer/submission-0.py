"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        curr = head
        while curr:
            newN = Node(curr.val, curr.next)
            curr.next = newN
            
            curr = curr.next.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        
        result = head.next
        curr = head
        while curr:
            currNext = curr.next.next
            if currNext:
                curr.next.next = currNext.next
            curr.next = currNext

            curr = curr.next

        return result