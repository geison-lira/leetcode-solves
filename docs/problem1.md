# LeetCodeSolves

## Problem 1 - Two Sum

### Solution Description
Given an array `nums` and an integer `target`, the optimal solution utilizes a Python Dictionary (or in other words, a **Hash Map**) to find the pair in a single pass. As we iterate through the list, we treat the dictionary as a look-back table.

For each element `num`, we check if it exists as a key in our dictionary.
* **If it exists**: We have found a previously visited number that, when added to the current `num`, equals the `target`. We return the stored index and the current `idx`
* **If it doesn't exist**: We calculate the complement `target - num` and store it as a key, with the current `idx` as its value. This "primes" the dictionary for future matches.

### Complexities and Clarity
* **Space Complexity**: The algorithm has space complexity of `O(n)`, where `n` is the length of the input array, because we store up to `n` elements in the dictionary.
* **Time Complexity**: The algorithm has time complexity of `O(n)`, where `n` is the length of the input array, because we traverse the list once and perform constant-time lookups.
* **Auxiliary Space**: The algorithm has auxiliary space complexity of `O(n)`, where `n` is the length of the input array, because the hash map grows proportionally to the input size.
* The implementation prioritizes readability by using clear variable names (`num`, `idx`) and straightforward control flow. It leverages Python’s dictionary for efficient lookups, avoiding nested loops and keeping the solution concise.
