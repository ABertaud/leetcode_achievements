class Solution:
    def build_list(self, last):
        newl = [1]
        for i in range(0, len(last) - 1, 1):
            newl.append(last[i] + last[i + 1])
        newl.append(1)
        return newl

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        nums = [[1], [1, 1]]
        numRows -= 2
        while numRows != 0:
            nums.append(self.build_list(nums[-1]))
            numRows -= 1
        return nums