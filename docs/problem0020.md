# LeetCodeSolves

## Problem 20 - Valid Parentheses

### Solution Description
Given a string `s`, the optimal solution utilizes a Python Dictionary to build a **Lookup Table**, where the key is an opening bracket and the value is its corresponding closing bracket. The solution also uses a **Stack**, to keep track of the correct closing bracket order. We then iterate through the string, and check whether the current character is an open bracket or not by checking if it's a key on the lookup dictionary.

* **If it is an open bracket**: We push its corresponding closing bracket onto the stack, so that the closing order is correctly tracked.
* **If it isn't an open bracket**: We check if the stack is empty, if it is, the string has an orphan closing bracket, meaning an invalid bracket order. Otherwise, we pop the top element of the stack and compare it with the current character, if they match, no further operations are done and we proceed to the next iteration, if they don't match, the string has an invalid bracket order.

By the end of the iterations, the stack should be empty for a valid string, meaning all brackets were correctly closed, if it's not empty, then the string has an invalid bracket order.

### Complexities and Clarity
* **Space Complexity**: The algorithm has space complexity of $O(n)$, where $n$ is the length of the input string, because in the worst case we can store up to $n$ elements in the stack.
* **Time Complexity**: The algorithm has time complexity of $O(n)$, where $n$ is the length of the input string, because we iterate through the string once and perform constant-time operations.
* The implementation prioritizes readability by using clear variable names (`stack`, `mapping`) and straightforward control flow. It leverages Python’s dictionary for efficient lookups, avoiding nested loops and keeping the solution concise.
