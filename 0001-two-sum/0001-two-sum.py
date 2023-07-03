class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i, nb in enumerate(nums):
            to_find = target - nb
            if to_find in nums_set:
                idx = nums.index(to_find)
                if idx != i:
                    return [i, nums.index(to_find)]
        return []