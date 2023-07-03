class Solution:
    def normalize(self, text):
	    return ''.join(c.lower() for c in text if c.isalnum())
    def isPalindrome(self, s: str) -> bool:
        toCompare = self.normalize(s)
        return toCompare == toCompare[::-1]
        