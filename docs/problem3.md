# LeetCodeSolves

## Problem 3 - Longest Substring Without Repeating Characters

### Solution Description
Given a string `s`, the optimal solution utilizes a **Sliding Window** approach. The limits of the sliding window are determined by two pointers: `start_idx` and `end_idx`. 

To optimize window adjustments, a Python Dictionary (`tracking`) keeps track of the last seen index of each character. As we iterate through the string with `end_idx`:

* **If the character is already in the dictionary:** It is a repeated character. The `start_idx` will update to the index immediately following the character's previous occurrence, provided that previous occurrence falls inside the current window. If it falls outside, `start_idx` remains unchanged.
* **If it is not in the dictionary:** `start_idx` remains unchanged.

After checking for duplicates, the character's index is updated in `tracking`. The `max_len` is then recalculated by taking the maximum of its current value and the current window size (`end_idx - start_idx + 1`).

### Complexities and Clarity
* **Space Complexity**: The algorithm has space complexity of `O(min(m, n))`, where `n` is the length of the input string and `m` is the size of the alphabet, because we store up to `n` or `m` elements in the dictionary, depending on whether the string is larger or smaller than the alphabet.
* **Time Complexity**: The algorithm has time complexity of `O(n)`, where `n` is the length of the input string, because we traverse the string exactly once.
* **Auxiliary Space**: The algorithm has auxiliary space complexity of `O(min(m, n))`, where `n` is the length of the input string and `m` is the size of the alphabet, for the same reasons as described in Space Complexity.
* The implementation prioritizes readability by using clear variable names (`start_idx`, `max_len`) and straightforward check-up and update logic. It leverages Python’s dictionary for efficient lookups, avoiding nested loops, and the `max()` function, to keep the solution concise.
