# LeetCodeSolves

## Problem 6 - Zigzag Conversion

### Solution Description
Given a string `s` and an integer `numRows`, the optimal solution utilizes a **List of Lists** data structure to store the characters of the string. It also utilizes the **Direction Toggling** strategy to store the characters in a zig-zag pattern. First, we check if `numRows` is one or if it's greater than the length of the string `s`, in either case, we can return `s` as is because zig-zag traversal does not occur. If not, we set an `idx` variable to `0` and a `step` variable to `-1`, we then iterate through each character of the string, appending the character to the sublist of index `idx` inside the superlist. We then check the value of `idx`.

* **If `idx == 0` or `idx == numRows-1`**: That means we reached the rows at the edges of the pattern, and we need to reverse traversal direction to maintain the zig-zag pattern. We do this by changing the sign of the variable `step`.
* **If not**: No further operations are needed.

At the end of each iteration, we add `step` to `idx`, depending on the value of `step`, `idx` can increase or decrease. After all iterations, we perform a double join operation to merge the characters within each row, and merge the rows into the final string.

### Complexities and Clarity
* **Space Complexity**: The algorithm has space complexity of $O(n)$, where $n$ is the length of the input string, because the list of lists will store all $n$ characters of the string. The solution could've utilized string concatenation by `+` instead of a list of lists, but because of how that operation works, it would not be truly $O(n)$, the `.join()` method is the optimal way to concatenate strings.
* **Time Complexity**: The algorithm has time complexity of $O(n)$, where $n$ is the length of the input string, because we traverse the string once and perform constant-time operations. Because the algorithm immediately returns if `numRows > len(s)`, the list comprehension loop will have $n$ iterations at maximum, so `numRows` does not affect the final $O(n)$ complexity, the same thing is true for the generator expression loop at the end of the algorithm.
* The implementation prioritizes readability by using clear variable names (`step`, `rows`) and straightforward control flow. It leverages Python's `.join()` method for efficient string concatenations, avoiding the use of `+` concatenation.
