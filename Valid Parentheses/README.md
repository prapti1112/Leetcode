# LeetCode 20: Valid Parentheses

## 📝 Problem Statement
Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid. A string is valid if open brackets are closed by the same type, in the correct order, and every close bracket has a corresponding open bracket. <br>

**Example 1:** s = "()" → **Output:** true <br>
**Example 2:** s = "([)]" → **Output:** false (Wrong order of closing) <br>
**Example 3:** s = "([])" → **Output:** true <br>

## 🚀 Algorithm: Stack-Based Matching
The algorithm uses a Stack data structure to keep track of the opening brackets. Since the last bracket opened must be the first one closed, the LIFO (Last-In, First-Out) property of a stack is ideal for this validation.


**The Logic**
* **Step 1: Initialization** — Create an empty stack and a hash map (dictionary) that pairs each closing bracket with its corresponding opening bracket.
* **Step 2: Iteration** — Traverse the string character by character. 
    * If the character is an **opening bracket**, push it onto the stack.
    * If the character is a **closing bracket**, check the top of the stack. If the stack is empty or the top element doesn't match the required opening bracket, return `false`.
* **Step 3: Final Validation** — After the loop, check if the stack is empty. If it is, return `true` (all brackets matched); otherwise, return `false` (some brackets remained unclosed).

## Analysis
* **Difficulty Level:** Easy
* **Runtime:** 0ms (Beats 100%)
* **Memory:** 19.40MB (Beats 8.83%)

## 🛠 Programming Paradigm
This solution follows the **Stack / Linear Scan** paradigm. <br>
* **LIFO Processing:** The stack ensures that we always validate the most recently opened scope before moving to the previous one.
* **Hash Map Lookups:** Using a dictionary for bracket pairs makes the code cleaner and allows for $O(1)$ mapping checks.

## 💡 Main Concepts Needed
1. **Stack (LIFO)**
   The core mechanism for managing nested structures.
2. **Hash Maps (Dictionaries)**
   Used to store pairs of brackets to avoid multiple `if-elif` statements, making the solution easily extendable to other bracket types.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the string, as we process each character exactly once. <br>
   **Space Complexity:** $O(n)$, in the worst case where the string consists entirely of opening brackets (e.g., `((((((`).