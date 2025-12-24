# LeetCode 121: Best Time to Buy and Sell Stock

## 📝 Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock. Return the maximum profit you can achieve; if no profit is possible, return 0. <br>

**Example 1:** prices = [7,1,5,3,6,4] → **Output:** 5 (Buy on day 2 at price 1 and sell on day 5 at price 6, profit = 6 - 1 = 5) <br>
**Example 2:** prices = [7,6,4,3,1] → **Output:** 0 (No transactions result in profit) <br>

## 🚀 Algorithm: Single-Pass Min-Max Tracking
The algorithm uses a greedy approach to track the lowest price (valley) encountered so far and calculates the potential profit against every subsequent price (peak). This ensures we satisfy the "buy before sell" constraint in a single linear scan.



**The Logic**
* **Step 1:** **Initialization** — Set two pointers, `min_id` and `max_id`, to the first day (index 0). Initialize `profit` to -1 (or 0) to track the best outcome found during the traversal.
* **Step 2:** **Dynamic Minimum Update** — Iterate through the array. If the current price is strictly lower than the price at `min_id`, reset both `min_id` and `max_id` to the current index. This effectively "restarts" our profit window because any future peak will yield more profit from this lower base.
* **Step 3:** **Profit Maximization** — If the current price is higher than the price at `max_id`, update `max_id`. At every step, calculate the difference between `prices[max_id]` and `prices[min_id]`. If this value exceeds our current global `profit`, update it.

## Analysis
* **Difficulty Level:** Easy
* **Runtime:** 62ms (Beats 74.09%)
* **Memory:** 26.31MB (Beats 96.91%)

## 🛠 Programming Paradigm
This solution follows the **Greedy** paradigm. <br>
* **Local Optimal State:** At any given day, we maintain the best possible "buy price" from the past.
* **One-Pass Efficiency:** By reducing the problem to a single scan, we avoid the $O(n^2)$ brute-force approach of checking every possible pair of days.

## 💡 Main Concepts Needed
1. **Pointers for State Management**
   Using indices (`min_id`, `max_id`) instead of storing actual values allows for easy tracking of the chronological "buy before sell" rule.
2. **Min-Tracking Logic**
   The realization that if we find a price lower than our current minimum, our previous "max" is no longer relevant for future calculations starting from the new minimum.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the `prices` array. We visit each element exactly once. <br>
   **Space Complexity:** $O(1)$, as we only store a fixed number of integer variables regardless of the input size.