class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        length = int(len(nums) / 2)
        nb = nums[length]
        if nb == target:
            return length
        elif nb > target and nums[length - 1] < target:
            return length
        elif nb < target and nums[length + 1] > target:
            return length + 1
        elif nb < target:
            return length + self.searchInsert(nums[length:], target)
        elif nb > target:
            return self.searchInsert(nums[:length], target)