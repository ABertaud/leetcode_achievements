class Solution:
    number_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinationsRecursive(self, digits: str, prefix: str) -> List[str]:
        l = []
        size = len(digits)
        if size == 1:
            for c in self.number_map[digits[0]]:
                l.append(prefix + c)
        elif size > 1:
            for c in self.number_map[digits[0]]:
                l += self.letterCombinationsRecursive(digits[1:], prefix + c)
        return l

    def letterCombinations(self, digits: str) -> List[str]:
        return self.letterCombinationsRecursive(digits, "")
