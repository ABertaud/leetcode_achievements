class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(0, len(nums) + 1):
            if not i in s:
                return i
        return 0