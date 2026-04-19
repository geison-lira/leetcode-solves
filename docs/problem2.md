# LeetCodeSolves

## Problem 2 - Add Two Numbers

### Solution Description
Given two linked lists `l1` and `l2`, the solution simulates digit-by-digit addition as in elementary arithmetic. At each step, we sum the current digits from both lists along with a carry from the previous step. A dummy head node is used to simplify list construction. We iterate while at least one list has remaining nodes or there is a non-zero carry. If a list is exhausted, its value is treated as 0.

At each iteration:
* Compute the sum of the two digits and the carry
* Create a new node with value `sum % 10`
* Update the carry as `sum // 10`
* Link the new node to the result list, and advance the `curr` pointer.

### Complexities and Clarity
* **Space Complexity**: The algorithm has space complexity of `O(max(m, n))`, where `m` is the size of the first list and `n` is the size of the second list, because we create a new list to store the sum digits.
* **Time Complexity**: The algorithm has time complexity of `O(max(m, n))`, where `m` is the size of the first list and `n` is the size of the second list, because we traverse each list once.
* **Auxiliary Space**: The algorithm has auxiliary space complexity of `O(1)`, because only a constant number of variables are used.
* The implementation prioritizes readability by using clear variable names (`curr`, `carry`) and straightforward control flow. It also leverages Python’s concise conditional expressions (e.g., `l1.val if l1 else 0`) to handle edge cases cleanly without extra branching.
