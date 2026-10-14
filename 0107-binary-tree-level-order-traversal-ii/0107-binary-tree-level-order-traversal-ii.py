# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []
        r = []
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            level=len(queue)
            c_level=[]
            for _ in range(level):
                a = queue.popleft()
                c_level.append(a.val)
                if a.left != None:
                    queue.append(a.left)
                if a.right != None:
                    queue.append(a.right)
            r.append(c_level)
        return r[::-1]
