# LeetCode 739: Daily Temperatures

## 📝 Problem Statement
Given an array of integers `temperatures`, return an array `answer` such that `answer[i]` is the number of days you have to wait after the $i^{th}$ day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`. <br>

**Example 1:** temperatures = [73,74,75,71,69,72,76,73] → **Output:** [1,1,4,2,1,1,0,0] <br>
**Example 2:** temperatures = [30,40,50,60] → **Output:** [1,1,1,0] <br>

## 🚀 Algorithm: Monotonic Decreasing Stack
The most efficient way to solve "next greater element" problems is using a monotonic stack. We maintain a stack of temperatures (and their indices) in decreasing order. When we encounter a temperature warmer than the one at the top of the stack, we have found the answer for those "waiting" days.



**The Logic**
* **Step 1: Initialize** — Create an `answer` array filled with zeros and an empty `stack`.
* **Step 2: Linear Scan** — Iterate through the temperatures. For each temperature, compare it with the top of the stack.
* **Step 3: Resolve Waiting Days** — While the current temperature is higher than the temperature at the top of the stack, it means the "wait" is over for that previous day. Pop the index from the stack and calculate the difference: `current_index - popped_index`.
* **Step 4: Push** — Push the current temperature and its index onto the stack to wait for a future warmer day.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 114ms (Beats 42.79%)
* **Memory:** 36.82MB (Beats 5.35%)

## 🛠 Programming Paradigm
This solution follows the **Monotonic Stack** paradigm. <br>
* **Efficient Look-back:** Instead of each day searching forward (which is slow), each day "resolves" as many previous days as possible in a single pass.
* **Amortized Complexity:** Each element is pushed and popped exactly once.

## 💡 Main Concepts Needed
1. **Monotonic Stack**
   A stack where elements are always sorted. In this case, we keep them in decreasing order to find the first element that "breaks" the order (the warmer day).
2. **Index Tracking**
   Storing the index in the stack is vital because the final answer requires the *distance* between days, not the temperature value itself.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, as each temperature is visited once and each index is pushed/popped at most once. <br>
   **Space Complexity:** $O(n)$, to store the stack in the worst case (a strictly decreasing list of temperatures).