# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorderidx = {val: idx for idx, val in enumerate(inorder)}
        def solve(left, right):
            if left > right:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            rootidx = inorderidx[root_val]
            root.right = solve(rootidx + 1, right)
            root.left = solve(left, rootidx - 1)
            return root

        return solve(0, len(inorder) - 1)
