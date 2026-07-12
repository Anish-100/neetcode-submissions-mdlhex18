# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Youtube Fix
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.var = True
        def dfs(curr):
            if curr is None:
                return 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            if not self.var:
                return 
            if abs(l-r) > 1:
                self.var = False
            return  1 + max(l,r)
        dfs(root)
        return self.var
        