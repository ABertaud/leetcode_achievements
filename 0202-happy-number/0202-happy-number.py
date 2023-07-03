class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while 1:
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n = int(n / 10)
            if tmp in s:
                return False
            s.add(tmp)
            if tmp == 1:
                return True
            n = tmp
        return False