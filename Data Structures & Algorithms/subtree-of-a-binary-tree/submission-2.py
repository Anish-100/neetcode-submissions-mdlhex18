# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return False
            if is_same_tree(root, subRoot):
                return True
            l = dfs(root.left)
            r = dfs(root.right)
            if l or r:
                return True
            return False

        def is_same_tree(root, sub_root):
            if root is None and sub_root is None:
                return True
            if root is None or sub_root is None or root.val != sub_root.val:
                return False
            l = is_same_tree(root.left, sub_root.left)
            r = is_same_tree(root.right, sub_root.right)
            if l and r:
                return True
            return False
        return dfs(root)