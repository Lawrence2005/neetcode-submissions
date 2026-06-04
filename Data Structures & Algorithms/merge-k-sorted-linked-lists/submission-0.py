# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        currLists = lists
        while len(currLists) > 1:
            newLists, lIndex = [], 0
            while lIndex < len(currLists):
                list1 = currLists[lIndex]
                list2 = currLists[lIndex + 1] if lIndex + 1 < len(currLists) else None
                print(list1, list2)
                newLists.append(self.merge2Lists(list1, list2))

                lIndex += 2

            currLists = newLists

        return currLists[0]
    
    def merge2Lists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        
        dummy = ListNode()
        curr = dummy

        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        curr.next = l1 if l1 else l2

        return dummy.next