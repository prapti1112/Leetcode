# LeetCode 75: Sort Colors

## 📝 Problem Statement
Given an array `nums` with $n$ objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue. <br>
We use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively. <br>

**Constraint:** You must solve this problem without using the library's sort function and ideally in a single pass. <br>

**Example 1:** nums = [2,0,2,1,1,0] → Output: [0,0,1,1,2,2] <br>
**Example 2:** nums = [2,0,1] → Output: [0,1,2] <br>

## 🚀 Algorithm: Dutch National Flag (Three-Pointer)
This problem is a classic application of the Dutch National Flag algorithm. We maintain three pointers to partition the array into four sections: zeros, ones, unclassified, and twos.



**The Logic**
* **Initialize Three Pointers:** * `low`: Points to where the next `0` should go (starts at index 0).
    * `mid`: The current element under consideration (starts at index 0).
    * `high`: Points to where the next `2` should go (starts at index $n-1$).
* **The Single Pass:** While `mid <= high`:
    * **If nums[mid] == 0:** Swap `nums[low]` and `nums[mid]`. Increment both `low` and `mid`.
    * **If nums[mid] == 1:** No swap needed. Just increment `mid`.
    * **If nums[mid] == 2:** Swap `nums[mid]` and `nums[high]`. Decrement `high`. (Do not increment `mid` yet, as the swapped element needs to be checked).

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** $O(n)$ — Each element is visited at most once.
* **Space:** $O(1)$ — Sorting is done in-place with no extra data structures.

## 🛠 Programming Paradigm
This solution follows the **Three-Way Partitioning** paradigm. <br>
* **In-place Mutation:** The algorithm rearranges elements within the original memory space, making it highly memory-efficient.
* **Invariant Maintenance:** At every step, the algorithm ensures that:
    1. Everything below `low` is `0`.
    2. Everything between `low` and `mid-1` is `1`.
    3. Everything above `high` is `2`.

## 💡 Main Concepts Needed
1. **Partitioning**
   Similar to the partitioning step in QuickSort, but specifically designed for cases where there are only a small number of unique keys (in this case, three: 0, 1, and 2).
2. **Pointer Logic (Why `mid` doesn't increment on 2s)**
   When we swap a `0` from the `mid` to the `low`, we know the element coming from `low` is a `1` (because `mid` already passed it), so we can move both pointers. However, when swapping a `2` to the `high`, the element coming from `high` is unknown, so we must inspect it again in the next iteration.
3. **Space/Time Complexity**
   **Time Complexity:** $O(n)$
   **Space Complexity:** $O(1)$