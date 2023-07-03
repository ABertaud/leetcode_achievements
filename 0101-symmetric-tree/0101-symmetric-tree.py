# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isTreeSymmetric(self, right, left):
        if not right and not left:
            return True
        if not left or not right:
            return False
        if right.val != left.val:
            return False
        return self.isTreeSymmetric(right.right, left.left) and self.isTreeSymmetric(right.left, left.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isTreeSymmetric(root.right, root.left)