# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.sum=float("-inf")
        def solve(root):
            if root==None:
                return 0
            leftSum=max(solve(root.left),0)
            rightSum=max(solve(root.right),0)
            currSum=root.val+leftSum+rightSum
            self.sum=max(self.sum,currSum)
            return root.val+max(leftSum,rightSum)
        solve(root)
        return self.sum