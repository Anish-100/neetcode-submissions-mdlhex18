# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n,min_val, max_val):
            if n is None:
                return True
            if not (min_val < n.val < max_val):
                return False
            return dfs(n.left, min_val, n.val) and dfs(n.right, n.val, max_val)
            
        return dfs(root,float('-inf'), float('inf'))