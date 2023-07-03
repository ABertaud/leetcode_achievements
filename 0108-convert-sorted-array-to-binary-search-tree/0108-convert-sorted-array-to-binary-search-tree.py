# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        l = int(len(nums) / 2)
        head = TreeNode(nums[l])
        if l != 0:
            head.left = self.sortedArrayToBST(nums[0:l])
            head.right = self.sortedArrayToBST(nums[l+1:])
        return head