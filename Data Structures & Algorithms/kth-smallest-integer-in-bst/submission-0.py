# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(nlogn) solution, not most optimal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        self.len = 0
        def dfs(root):
            if root is None:
                return None
            dfs(root.left)
            dfs(root.right)
            nums.append(root.val)
            self.len+=1
        dfs(root)
        nums.sort()
        return nums[k-1]
            


        