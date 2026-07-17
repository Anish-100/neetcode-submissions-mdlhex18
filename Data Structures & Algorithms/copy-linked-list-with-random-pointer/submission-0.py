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
        freq_map = {}
        new_map = {}
        new_head = Node(0)
        i = 0
        curr = head
        prev = new_head
        while curr:
            freq_map[curr] = i
            prev.next = Node(curr.val, None, None)
            prev = prev.next
            new_map[i] = prev
            i+=1
            curr = curr.next
        curr = new_head.next
        tmp = head
        while curr:
            if tmp.random in freq_map:
                idx = freq_map[tmp.random]
                curr.random = new_map[idx]
            else:
                curr.random = None
            curr = curr.next
            tmp = tmp.next
        return new_head.next

            
        

        
            


        