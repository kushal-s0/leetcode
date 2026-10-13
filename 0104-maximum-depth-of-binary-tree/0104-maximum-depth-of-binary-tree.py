# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        node=root
        if node==None:
            return 0
        lh=self.maxDepth(node.left)
        rh=self.maxDepth(node.right)
        return 1+max(lh,rh)