class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nb = 0
        i = 0
        length = len(nums)
        while nb + i != length:
            if nums[i] == 0:
                nb += 1
                del nums[i]
                i -= 1
            i += 1
        while nb != 0:
            nums.append(0)
            nb -= 1