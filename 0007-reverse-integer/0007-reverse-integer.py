class Solution:
    def reverse(self, x: int) -> int:
        nb = 0
        sub = False
        if x < 0:
            sub = True
            x = abs(x)
        while x > 0:
            nb += x % 10
            if x > 9:
                nb *= 10
            x = int(x / 10)
        if sub:
            nb = nb * -1
        if nb > 2**31-1 or nb < -2**31:
            return 0
        return nb