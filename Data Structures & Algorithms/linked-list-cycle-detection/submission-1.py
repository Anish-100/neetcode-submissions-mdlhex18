# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        l = head
        r = head.next.next
        while l is not None and r is not None:
            if l == r:
                return True
            if r.next != None:
                r = r.next.next
            else:
                return False
            l = l.next
        return False
        