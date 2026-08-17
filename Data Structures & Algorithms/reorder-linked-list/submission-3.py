# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr:
            length+=1
            curr = curr.next
        curr = head
        i = 0
        rev_head = None
        while curr:
            if i == math.ceil(length/2):
                rev_head = self.reverse(curr)
                break
            i+=1
            curr = curr.next
        curr = head
        prev = ListNode()
        while curr and rev_head:
            prev.next = curr
            tmp = curr.next
            curr.next = rev_head
            prev = rev_head
            rev_head = rev_head.next
            curr = tmp
        if curr is not None:
            prev.next = curr
            curr.next  = None
    def reverse(self,head):
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            head = curr
            prev = curr
            curr = tmp
        
        return head

