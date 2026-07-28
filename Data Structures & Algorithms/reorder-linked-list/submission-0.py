# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        freqMap = {}
        curr,n = head,0
        while curr:
            freqMap[n] = curr
            curr = curr.next
            n+=1
        curr = head
        for i in range(1,(n//2)+1):
            curr.next = freqMap[n-i]
            if n-i == i:
                freqMap[n-i].next = None
                break
            freqMap[n-i].next = freqMap[i]
            curr = freqMap[i]
        if n%2 == 1:
            curr.next = freqMap[n//2]
            freqMap[n//2].next = None
