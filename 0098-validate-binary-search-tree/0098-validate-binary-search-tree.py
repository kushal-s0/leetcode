# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a=[]
        self.inorder(root,a)
        for i in range(len(a)-1):
            if a[i]>=a[i+1]:
                return False
        return True
    def inorder(self,root,a):
        if root is None:
            return
        self.inorder(root.left,a)
        a.append(root.val)
        self.inorder(root.right,a)
        