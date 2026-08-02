# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(root):
            nonlocal max_sum
            if root is None:
                return 0
            l = max(dfs(root.left),0)
            r = max(dfs(root.right),0)
            max_sum = max(max_sum,root.val + l+r)
            return root.val+ max(l,r)
        dfs(root)
        return max_sum
        