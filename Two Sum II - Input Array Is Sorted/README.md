# LeetCode 167: Two Sum II - Input Array Is Sorted

## 📝 Problem Statement
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. <br>
Let these two numbers be `numbers[index1]` and `numbers[index2]` where $1 \le index1 < index2 \le numbers.length$. <br>
Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2. <br>

**Example 1:** numbers = [2,7,11,15], target = 9 → Output: [1,2] (2 + 7 = 9) <br>
**Example 2:** numbers = [2,3,4], target = 6 → Output: [1,3] (2 + 4 = 6) <br>
**Example 3:** numbers = [-1,0], target = -1 → Output: [1,2] (-1 + 0 = -1) <br>

## 🚀 Algorithm: Two-Pointer Technique
Since the array is already sorted, we can find the target sum efficiently without using a Hash Map or nested loops.



**The Logic**
* **Initialize Two Pointers:** Place `left` at the start (index 0) and `right` at the end (index $n-1$) of the array.
* **Calculate Sum:** Compute $current\_sum = numbers[left] + numbers[right]$.
* **Comparison:**
    * If $sum == target$: We found the answer! Return `[left + 1, right + 1]`.
    * If $sum < target$: We need a larger sum. Since the array is sorted, we move the `left` pointer to the right to increase the value.
    * If $sum > target$: We need a smaller sum. We move the `right` pointer to the left to decrease the value.
* **Termination:** Because the problem guarantees exactly one solution, the pointers will eventually meet at the correct pair.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** $O(n)$ — We traverse the array at most once.
* **Memory:** $O(1)$ — We only use two variables for pointers, satisfying the constant extra space constraint.

## 🛠 Programming Paradigm
This solution follows the **Two-Pointer** paradigm. <br>
* **Sorted Property:** This paradigm leverages the fact that the input is sorted. By moving pointers based on the sum's relation to the target, we effectively "shrink" the search space.
* **Greedy Selection:** At each step, we make a local decision (move left or move right) that brings us closer to the global solution without needing to backtrack.

## 💡 Main Concepts Needed
1. **1-Indexed Arrays**
   The problem asks for 1-based indexing. Since most programming languages (like Python) use 0-based indexing, we must add 1 to our final indices before returning.
2. **Binary Search vs. Two Pointers**
   While Binary Search could be used for each element ($O(n \log n)$), the Two-Pointer approach is more efficient ($O(n)$) and takes advantage of the "sorted" constraint perfectly.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the array. <br>
   **Space Complexity:** $O(1)$, as we do not store any additional data structures like Hash Maps.