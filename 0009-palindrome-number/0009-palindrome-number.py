class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while reversed_num < x:
            reversed_num = reversed_num * 10 + int(x % 10)
            x = int(x / 10)
        return reversed_num == x or x == int(reversed_num / 10)