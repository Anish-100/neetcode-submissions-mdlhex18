# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        node1 = list1
        node2 = list2

        if node1.val < node2.val:
            head = node1
            prev = node1
            node1 = node1.next
        else:
            head = node2
            prev = node2
            node2 = node2.next
        while node1 != None and node2 != None:
            if node1.val < node2.val:
                prev.next = node1
                prev = prev.next
                node1 = node1.next
            else:
                prev.next = node2
                prev = prev.next
                node2 = node2.next
        if node1 != None:
            while node1 is not None:
                prev.next = node1
                prev = prev.next
                node1 = node1.next
        elif node2 != None:
            while node2 is not None:
                prev.next = node2
                prev = prev.next
                node2 = node2.next
        return head


                




