class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        nb = digits[-1]
        if nb != 9:
            digits[-1] += 1
        else:
            retained = True
            for i in range(len(digits) - 1, -1, -1):
                digits[i] += retained
                retained = False
                if digits[i] == 10:
                    digits[i] = 0
                    retained = True
            if retained == True:
                digits.insert(0, 1)
        return digits