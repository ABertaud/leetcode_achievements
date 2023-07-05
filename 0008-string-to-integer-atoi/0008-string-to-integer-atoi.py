class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        idx = 0
        positive = 1
        l = len(s)
        while idx != l and s[idx] == ' ':
            idx += 1
        if idx != l and s[idx] == '-':
            positive *= -1
            idx += 1
        elif idx != l and s[idx] == '+':
            positive *= 1
            idx += 1
        while idx != l and s[idx].isdigit():
            if result > 0:
                result *= 10
            result += ord(s[idx]) - 48
            idx += 1
        if result > 2147483647:
            if positive < 0:
                result = 2147483648
            else:
                result = 2147483647
        return result * positive
        