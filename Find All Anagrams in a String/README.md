# LeetCode 438: Find All Anagrams in a String

## 📝 Problem Statement
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. An anagram is a string formed by rearranging the letters of another string, typically using all the original letters exactly once. <br>

**Example 1:** s = "cbaebabacd", p = "abc" → **Output:** [0, 6] (Indices 0: "cba" and 6: "bac" are anagrams of "abc") <br>
**Example 2:** s = "abab", p = "ab" → **Output:** [0, 1, 2] (Indices 0: "ab", 1: "ba", and 2: "ab" are all anagrams) <br>

## 🚀 Algorithm: Brute Force Sliding Window with Sorting
The algorithm uses a sliding window of fixed length (equal to the length of `p`) to traverse string `s`. At each step, it extracts the current substring and compares its sorted version to the sorted version of `p`. If they match, the current starting index is an anagram position.



**The Logic**
* **Step 1:** **Target Preparation** — Sort string `p` once at the beginning to create a canonical reference for comparison.
* **Step 2:** **Window Traversal** — Iterate through string `s` using a `range` that allows a window of length `len(p)` to slide across without going out of bounds.
* **Step 3:** **Substring Validation** — In each iteration, slice the current window from `s`, sort it, and compare it to the sorted `p`. If equal, append the `start_index` to the results list.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 7447 ms (Beats 5.02%)
* **Memory:** 19.70 MB (Beats 11.64%)

## 🛠 Programming Paradigm
This solution follows the **Sliding Window (Fixed Size)** paradigm. <br>
* **Sub-problem Isolation:** The problem is broken down into checking every possible substring of length $K$.
* **Canonical Form Comparison:** By sorting both the target and the window, the algorithm simplifies the anagram check into a simple string equality check.

## 💡 Main Concepts Needed
1. **String Slicing**
   Utilized to extract a specific portion of string `s` based on the current `start_index` and the required length of `p`.
2. **Canonical Form (Sorting)**
   Sorting is a common way to identify anagrams. Two strings are anagrams if and only if their sorted versions are identical.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(N \cdot K \log K)$, where $N$ is the length of `s` and $K$ is the length of `p`. For every index in `s`, we perform a sort on a substring of length $K$. <br>
   **Space Complexity:** $O(K)$, to store the sorted versions of the substrings and string `p`.