# Imports (just for testing, DO NOT COPY THESE)
from typing import List


# Actual solution below
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffs = {}

        for idx, num in enumerate(nums):
            if num in diffs.keys():
                return [diffs[num], idx]

            diffs[target - num] = idx
