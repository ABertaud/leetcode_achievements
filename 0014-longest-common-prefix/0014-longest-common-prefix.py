class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        to_return = ""
        idx = 0
        length = len(strs[0])
        while 1:
            if idx == length:
                return to_return
            to_return += strs[0][idx]
            for str in strs:
                if not str.startswith(to_return):
                    to_return = to_return[:-1]
                    return to_return
            idx += 1
        return to_return