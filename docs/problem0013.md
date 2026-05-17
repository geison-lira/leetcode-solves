# LeetCodeSolves

## Problem 13 - Roman to Integer

### Solution Description
Given a string `s`, the optimal solution utilizes a Python Dictionary to build a **Lookup Table**, where the key is the Roman numeral and the value is its corresponding decimal value. Then, it iterates through each character of the Roman numeral string, the variable `curr` stores the decimal value of the character currently being processed while the variable `prev` stores the decimal value of the previously processed character. The value of `curr` is then added to the final result variable `num`. Roman numerals are always written from the largest numeral to the smallest one, so we compare the current numeral `curr` with the previous one `prev`.

* **If `curr > prev`**: That means a subtractive case occurred, so the previous numeral should be subtracted from the current one. Given that we have already added the previous numeral to the final result, we should subtract twice the value of the previous numeral, to get the correct result. 
* **If `curr <= prev`**: That means the expected additive case occurred, and no further action is needed.

Lastly, `prev` is updated to the current value `curr` to be used in the next iteration.

### Complexities and Clarity
* **Space Complexity**: The algorithm has space complexity of $O(1)$, because the lookup dictionary only stores the Roman numerals and its corresponding decimal values, which is a constant amount of space.
* **Time Complexity**: The algorithm has time complexity of $O(n)$, where $n$ is the length of the input string, because we iterate through the string once and perform constant-time lookups.
* The implementation prioritizes readability by using clear variable names (`num`, `prev`) and straightforward control flow. It leverages Python’s dictionary for efficient lookups, avoiding nested loops and keeping the solution concise.
