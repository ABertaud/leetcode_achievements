class Solution:
    def fillBinary(self, s):
        for i in range(len(s), 32):
            s = '0' + s
        return s
    def reverseBits(self, n: int) -> int:
        s = self.fillBinary(bin(n)[2:])
        return int(s[::-1], 2)