class Solution:
    def isPalindrome(self, s: str):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        to_return = ""
        for i in range(len(s)):
            tmp_str = "" + s[i]
            for j in range(i + 1, len(s)):
                tmp_str += s[j]
                if self.isPalindrome(tmp_str):
                    if len(tmp_str) > len(to_return):
                        to_return = tmp_str
        if to_return == "":
            return s[0]
        return to_return
