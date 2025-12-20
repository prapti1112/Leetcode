# LeetCode 238: Product of Array Except Self

## 📝 Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. <br>
The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. <br>

**Constraint:** You must write an algorithm that runs in $O(n)$ time and **without** using the division operation. <br>

**Example 1:** nums = [1,2,3,4] → Output: [24,12,8,6] <br>
**Example 2:** nums = [-1,1,0,-3,3] → Output: [0,0,9,0,0] <br>

## 🚀 Algorithm: Prefix and Suffix Product (Two-Pass)
Since we cannot use division, we realize that for any index $i$, the result is the product of all numbers to its left multiplied by all numbers to its right.



**The Logic**
* **Left Pass (Prefix):** We traverse the array from left to right. We use a variable `prefix` to keep track of the running product and store it in our result array. `res[i]` will contain the product of all elements from `nums[0]` to `nums[i-1]`.
* **Right Pass (Suffix):** We traverse the array from right to left. We use a variable `suffix` to keep track of the running product of elements to the right. We multiply the existing value in `res[i]` by this `suffix` value.
* **Optimization:** By using the output array to store the prefix products and a single variable for the suffix, we satisfy the $O(1)$ extra space follow-up.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** $O(n)$ — We iterate through the array twice (2n passes).
* **Space:** $O(1)$ — Excluding the output array, we only use two integer variables (`prefix` and `suffix`).

## 🛠 Programming Paradigm
This solution utilizes the **Prefix Sum / Functional Array** paradigm (specifically for products). <br>
* **Preprocessing:** Instead of recalculating the product for every index (which would be $O(n^2)$), we pre-calculate the "context" (left and right products) in linear time.
* **Space-Efficient Iteration:** We transform a potential $O(n)$ space complexity (using two separate prefix/suffix arrays) into $O(1)$ by updating the result array in-place during the second pass.

## 💡 Main Concepts Needed
1. **The Division Trap**
   While $TotalProduct / nums[i]$ seems intuitive, it fails if the array contains a `0` (division by zero error) and is explicitly forbidden by the problem constraints.
2. **Identity Element of Multiplication**
   We initialize our `prefix` and `suffix` trackers to `1` because multiplying by 1 does not change the product, allowing us to handle the edges of the array (index 0 and index $n-1$) safely.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the array. <br>
   **Space Complexity:** $O(1)$ extra space (as per LeetCode's rule that the output array does not count toward complexity).