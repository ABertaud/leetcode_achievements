from collections import deque

class Solution:
    def isCloser(self, c):
        return c == ')' or c == ']' or c == '}'

    def isOpener(self, c):
        return c == '(' or c == '[' or c == '{'

    def isMatch(self, c, d):
        if c == '(' and d == ')':
            return True
        elif c == '[' and d == ']':
            return True
        elif c == '{' and d == '}':
            return True
        return False
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length == 0 or (length % 2) == 1 or self.isCloser(s[0]):
            return False
        current_opened = deque()
        for c in s:
            if self.isOpener(c) == True:
                current_opened.appendleft(c)
            elif self.isCloser(c) == True and current_opened and self.isMatch(current_opened[0], c):
                current_opened.popleft()
            else:
                return False
        if current_opened:
            return False
        return True
    