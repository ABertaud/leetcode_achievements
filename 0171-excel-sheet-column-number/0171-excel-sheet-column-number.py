class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) <= 0:
            return 0
        col = ord(columnTitle[0]) - 64
        for i in range(1, len(columnTitle)):
            col = (ord(columnTitle[i]) - 64) + (col * 26)
        return col
