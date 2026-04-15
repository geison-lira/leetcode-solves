# LeetCodeSolves

## Problem 1 - Two Sum

### Solution Description
Given an array `nums` and an integer `target`, the optimal solution utilizes a Python Dictionary (or in other words, a **Hash Map**) to find the pair in a single pass. As we iterate through the list, we treat the dictionary as a look-back table.

For each element `num`, we check if it exists as a key in our dictionary.
* **If it exists**: We have found a previously visited number that, when added to the current `num`, equals the `target`. We return the stored index and the current `idx`
* **If it doesn't exist**: We calculate the complement `target - num` and store it as a key, with the current `idx` as its value. This "primes" the dictionary for future matches.

### Complexities and Clarity
* The algorithm has space complexity of `O(n)`, because in the worst case, it creates a dictionary of the same size of the input array.
* The algorithm has time complexity of `O(n)`, because in the worst case, it needs to access all elements of the input array.
* The code aimed to be as pythonic and clear as possible, using existing native methods and meaningful syntax.
