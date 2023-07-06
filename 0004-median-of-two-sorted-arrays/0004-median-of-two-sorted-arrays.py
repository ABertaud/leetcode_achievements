class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        total = len(nums1) + len(nums2)
        half = total // 2
        start, end = 0, len(nums1) - 1
        while True:
            i = (start + end) // 2  # cut from nums1
            j = half - i - 2  # cut from nums2

            firstL = nums1[i] if i >= 0 else float("-infinity")
            firstR = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            secondL = nums2[j] if j >= 0 else float("-infinity")
            secondR = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if firstL <= secondR and secondL <= firstR:
                # odd
                if total % 2:
                    return min(firstR, secondR)
                # even
                return (max(firstL, secondL) + min(firstR, secondR)) / 2
            elif firstL > secondR:
                end = i - 1
            else:
                start = i + 1
        return -1