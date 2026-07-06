# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        carry_over = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry_over
            carry_over = temp // 10
            if not head:
                head = ListNode(temp%10, None)
                curr = head
            else:
                curr.next = ListNode(temp%10, None)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp = l1.val + carry_over
            curr.next = ListNode(temp%10, None)
            curr = curr.next
            carry_over = temp // 10
            l1 = l1.next
        while l2: 
            temp = l2.val + carry_over
            curr.next = ListNode(temp%10, None)
            curr = curr.next
            carry_over = temp // 10
            l2 = l2.next
        if carry_over:
            curr.next = ListNode(carry_over, None)
            curr = curr.next

        return head
           
