# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        llen = 0
        curr = head
        while curr:
            llen+=1
            curr = curr.next
        n = (llen - n) 
        i = 0
        dummy = ListNode()
        prev = dummy
        curr = head
        while curr:
            if i == n:
                prev.next = curr.next

            else:
                prev.next = curr
                prev = prev.next
            curr = curr.next
            i+=1
        return dummy.next

        