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
            l = dfs(root.left)
            r = dfs(root.right)
            curr = root.val
            new = []
            if l >= 0:
                curr +=l
                new.append(l)
            if r >= 0:
                curr +=r
                new.append(r)
            max_sum = max(curr, max_sum)
            if new:
                return max(new) + root.val
            return root.val
        dfs(root)
        return max_sum
        