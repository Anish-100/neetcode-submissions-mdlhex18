# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        def dfs(root):
            m,n = False, False
            if root is None:
                return None,None
            a,b = dfs(root.left)
            c,d = dfs(root.right)
            if root.val == p.val or (a or c):
                m = True
            if root.val == q.val or (b or d):
                n = True
            if m and n:
                self.res = root
                return False, False
            if a or c:
                m= True
            if b or d:
                n = True
            return m,n
        dfs(root)
        return self.res