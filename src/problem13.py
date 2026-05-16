# Actual solution below
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        prev = 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for char in s:
            curr = mapping[char]
            num += curr
            if curr > prev:
                num -= 2 * prev
            prev = curr
        return num
