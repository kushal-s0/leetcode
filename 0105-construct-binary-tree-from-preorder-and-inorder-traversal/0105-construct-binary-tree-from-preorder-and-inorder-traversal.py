# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorderidx = {val: idx for idx, val in enumerate(inorder)}
        preorder_queue = deque(preorder)


        def solve(left, right):
            if left > right:
                return None
            root_val = preorder_queue.popleft()
            root = TreeNode(root_val)
            rootidx = inorderidx[root_val]
            root.left = solve(left, rootidx - 1)
            root.right = solve(rootidx + 1, right)
            return root

        return solve(0, len(inorder) - 1)
