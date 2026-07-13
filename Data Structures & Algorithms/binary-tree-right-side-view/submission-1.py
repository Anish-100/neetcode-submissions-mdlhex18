# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            len_q = len(q)
            last = None
            for _ in range(len_q):
                n = q.popleft()
                last = n
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
            res.append(last.val)
        return res
        