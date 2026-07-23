# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Plan:
# Go through k nodes, put it through a reverse helper function maintaining a i throughout
# Set a dummy to None.
# new_head is what is returned from the the rev helper
# prev = last node while reversing
# Reverse returns both new_head and tail
# If i ends before k, rev it use .next is None as the main while lop


# A more efficient solution O(n)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lenL = 0
        curr = head
        # Get total length
        while curr:
            lenL +=1
            curr = curr.next
        curr = head


        dummy = ListNode(0, None)
        i = 0
        l = 0
        prevTail = dummy
        prevHead = curr
        prev = None
        while curr:
            i+=1
            l+=1
            nxt = curr.next
            curr.next = prev
            prev = curr
            if i == k:
                prevTail.next = curr
                prevHead.next = nxt
                prevTail = prevHead
                prevHead = prevHead.next
                i = 0
                if lenL - l < k:
                    break
            curr = nxt
        return dummy.next

        