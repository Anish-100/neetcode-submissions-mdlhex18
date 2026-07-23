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

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = None
        curr = head
        i = 0
        prevTail = ListNode(0, None)
        prevHead= curr
        while curr:
            i+=1
            if i == k:
                if dummy is None:
                    dummy = curr
                nxt = curr.next
                nHead ,tail = self.revLinkedList(prevHead,k)
                prevTail.next = nHead
                prevTail = tail
                tail.next = nxt
                prevHead = nxt
                curr = nxt
                i = 0
            else:
                curr = curr.next
        return dummy

    def revLinkedList(self, head, k):
        prev = None
        tail = None
        curr = head
        newHead = curr
        i = 0
        while i < k:
            if tail is None:
                tail = curr
            nxt = curr.next
            curr.next = prev
            prev = curr
            newHead = curr
            curr = nxt
            i+=1
        return newHead, tail

        