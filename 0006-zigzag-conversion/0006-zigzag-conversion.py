class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_cpt = 0
        climbing = True
        array = {}
        for c in s:
            if not zigzag_cpt in array:
                array[zigzag_cpt] = ""
            array[zigzag_cpt] += c
            if climbing == True:
                zigzag_cpt += 1
            else:
                zigzag_cpt -= 1
            if zigzag_cpt == 0:
                climbing = True
            elif zigzag_cpt == (numRows - 1):
                climbing = False
        return ''.join(value for value in array.values())