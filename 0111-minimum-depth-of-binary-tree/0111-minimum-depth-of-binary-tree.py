# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        rightDepth = self.minDepth(root.right)
        leftDepth = self.minDepth(root.left)
        if rightDepth == 0:
            rightDepth = leftDepth
        elif leftDepth == 0:
            leftDepth = rightDepth
        return min(rightDepth, leftDepth) + 1