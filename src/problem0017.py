# Imports (just for testing, DO NOT COPY THESE)
from typing import List


# Actual solution below
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = []
        path = []

        def backtrack(idx: int):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            for char in mapping[digits[idx]]:
                path.append(char)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)
        return combinations
