# LeetCode 152: Maximum Product Subarray
## 📝 Problem Statement
Given an integer array nums, find a subarray (a contiguous part of the array) that has the largest product, and return that product. <br>
The test cases are generated so that the answer will fit in a 32-bit integer. <br>
Example 1: nums = [2,3,-2,4] → Output: 6 (Subarray [2,3]) <br>
Example 2: nums = [-2,0,-1] → Output: 0 (Subarray [-2,0,-1] is not possible, and [-2,-1] is not contiguous) <br>

## 🚀 Algorithm: Optimized Min-Max Tracking
The most efficient way to solve this is an adaptation of Kadane’s Algorithm. While the standard Kadane's handles sums, the product version must account for negative numbers. <br>
The Logic <br>
* <b>Track Two States:</b> Maintain both a current_max and a current_min.
* <b>The Negative Flip:</b> When we encounter a negative number, the current_max could become the new current_min and vice versa.
* <b>The Restart:</b> At each element, we decide whether to include the previous product or "start fresh" from the current element. This is handled by:
$$current\_max = \max(n, n \cdot current\_max, n \cdot current\_min)$$
* <b>Zero Handling:</b> Zeros naturally reset the product chain, forcing the algorithm to start fresh at the next non-zero element.


## Analysis
* <b>Difficulty Level: </b> Medium
* <b>Runtime: </b> 10ms (Beats 58.98%)
* <b>Money: </b> 18.14MB (Beats 96.05%)


## 🛠 Programming Paradigm
This solution follows the Dynamic Programming (DP) paradigm. <br>
* <b>Optimal Substructure:</b> The maximum product ending at index $i$ can be computed using the results (max and min) from index $i-1$.
* <b>Overlapping Subproblems:</b> We solve the same problem (finding the best product) for smaller prefixes of the array to build up to the final answer.
* <b>Space Optimization:</b> Instead of an entire DP table/array, we use Tabulation with Space Optimization, reducing the space complexity from $O(n)$ to $O(1)$ by only storing the previous state.

## 💡 Main Concepts Needed
1. Contiguous Subarrays
Unlike "subsequences," subarrays must be connected. This means we cannot simply pick all negative numbers to make them positive; they must be adjacent.
2. Properties of Multiplication
Positive × Positive = Positive (Increases magnitude)
Negative × Negative = Positive (Can turn a very small number into a very large one)
Any × Zero = Zero (Resets the product)
3. Space/Time Complexity
Time Complexity: $O(n)$, where $n$ is the length of the array. We visit each element exactly once.
Space Complexity: $O(1)$. We only use a constant amount of extra space for three variables (res, curMax, curMin).
