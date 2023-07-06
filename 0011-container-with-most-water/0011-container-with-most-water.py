class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        right_decrease = False
        capacity = 0
        while i != j:
            if height[i] > height[j]:
                right_decrease = True
            else:
                right_decrease = False
            if right_decrease == True:
                capacity = max(capacity, height[j] * (j - i))
                j -= 1
            else:
                capacity = max(capacity, height[i] * (j - i))
                i += 1
        return capacity
