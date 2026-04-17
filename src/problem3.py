# Solution below
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start_idx = 0
        tracking = {}
        for end_idx, char in enumerate(s):
            if char in tracking:
                start_idx = max(start_idx, tracking[char] + 1)
            tracking[char] = end_idx
            max_len = max(max_len, end_idx - start_idx + 1)
        return max_len
