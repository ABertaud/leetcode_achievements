class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nb = 0
        i = 0
        length = len(nums)
        while i < length:
            tmp_nb = nums[i]
            nums[nb] = tmp_nb
            nb += 1
            while i != length and nums[i] == tmp_nb:
                i += 1
        return nb