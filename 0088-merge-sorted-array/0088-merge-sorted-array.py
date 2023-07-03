class Solution:
    def clean_zeros(self, l, n):
        for i in range(len(l) - 1, len(l) - n - 1, -1):
            l.pop(i)
        return l

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = 0
        second_one = 0
        nums1 = self.clean_zeros(nums1, n)
        for second_one in range(n):
            while start != len(nums1) and nums1[start] < nums2[second_one]:
                start += 1
            nums1.insert(start, nums2[second_one])