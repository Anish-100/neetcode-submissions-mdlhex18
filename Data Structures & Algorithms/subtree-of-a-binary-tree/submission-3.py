# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = deque([root])

        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if self.dfs(n, subRoot):
                    return True
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
        return False


    def dfs(self,tree, subTree):
        if tree is None and subTree is None:
            return True
        if tree is None or subTree is None:
            return False
        if tree.val != subTree.val:
            return False
        return self.dfs(tree.right, subTree.right) and self.dfs(tree.left, subTree.left)
        
