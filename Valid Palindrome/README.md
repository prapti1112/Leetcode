# LeetCode 125: Valid Palindrome

## 📝 Problem Statement
Given a string `s`, determine if it is a palindrome after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters. A palindrome reads the same forward and backward. <br>

**Example 1:** s = "A man, a plan, a canal: Panama" → **Output:** true ("amanaplanacanalpanama" is the same forwards and backwards) <br>
**Example 2:** s = "race a car" → **Output:** false (After cleaning, "raceacar" does not match its reverse "racaecar") <br>

## 🚀 Algorithm: Regex Normalization & String Slicing
This approach focuses on high readability and leverages Python's optimized internal C-functions for string manipulation and reversal.



**The Logic**
* **Step 1:** **Normalization** — Convert the string to lowercase and use the Regex pattern `[^a-zA-Z0-9]` to replace all non-alphanumeric characters with an empty string.
* **Step 2:** **Reversal** — Create a reversed version of the cleaned string using Python’s efficient slicing syntax `s[::-1]`.
* **Step 3:** **Comparison** — Perform a direct equality check between the normalized string and its reversed counterpart, returning the boolean result.

## Analysis
* **Difficulty Level:** Easy
* **Runtime:** 7ms (Beats 82.89%)
* **Memory:** 19.20MB (Beats 24.91%)

## 🛠 Programming Paradigm
This solution follows the **String Preprocessing & Functional** paradigm. <br>
* **Data Sanitization:** By cleaning the data into a "canonical form" first, we reduce a complex problem with multiple edge cases (spaces, punctuation, casing) into a simple equality check.
* **Declarative Approach:** Instead of manually managing pointers and state, we describe *what* we want (a cleaned, reversed string) and let the language's built-in methods execute it efficiently.

## 💡 Main Concepts Needed
1. **Regular Expressions (Regex)**
   Regex is essential for pattern matching. Using `re.sub` allows for the bulk removal of unwanted characters without writing manual conditional loops.
2. **Python Slicing Syntax**
   Slicing `[start:stop:step]` is a fundamental Python tool. Setting the step to `-1` is the standard, optimized way to reverse a sequence.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the string. Normalization and reversal both require a single pass over the data. <br>
   **Space Complexity:** $O(n)$, as we generate a new cleaned string and a reversed copy, both proportional to the input size.