class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        set_s = set()
        window_start = 0
        window_end = 0
        while window_end != len(s):
            if s[window_end] in set_s:
                set_s.remove(s[window_start])
                window_start += 1
            else:
                set_s.add(s[window_end])
                window_end += 1
                max_len = max(window_end - window_start, max_len)
        return max_len