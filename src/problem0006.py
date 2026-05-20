class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        idx = 0
        step = -1
        for char in s:
            rows[idx].append(char)
            if idx == 0 or idx == numRows - 1:
                step *= -1
            idx += step
        return "".join("".join(row) for row in rows)
