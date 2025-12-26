# LeetCode 3: Longest Substring Without Repeating Characters

## 📝 Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters. <br>

**Example 1:** s = "abcabcbb" → **Output:** 3 (The substring is "abc") <br>
**Example 2:** s = "pwwkew" → **Output:** 3 (The substring is "wke") <br>

## 🚀 Algorithm: Dynamic List-Based Sliding Window
This approach maintains a list that acts as a "active" window of unique characters. When a duplicate is encountered, the window is "cut" to remove the old instance of the character and everything before it, allowing the window to continue growing from the first unique point.



**The Logic**
* **Step 1:** **Initialization** — Create an empty list `substring` to store the current window of unique characters and a variable `longest_sub_len` to track the maximum length found.
* **Step 2:** **Duplicate Detection & Slicing** — Iterate through the string. If the current character is already in the `substring` list, find its index, slice the list to remove that character and all preceding characters, and then append the new character.
* **Step 3:** **Expansion & Comparison** — If the character is not a duplicate, simply append it to the list. After each character is processed, update `longest_sub_len` if the current list length is greater than the record.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 20ms (Beats 37.53%)
* **Memory:** 17.45MB (Beats 92.67%)

## 🛠 Programming Paradigm
This solution follows the **Sliding Window** paradigm. <br>
* **Variable Window Size:** The window (represented by the list) expands as we find new unique characters and shrinks dynamically when a duplicate is found.
* **In-Place Substring Maintenance:** Instead of checking all possible substrings, we maintain a single moving reference of the current valid substring.

## 💡 Main Concepts Needed
1. **List Slicing**
   Crucial for "resetting" the window. Slicing `substring[cut_ind:]` efficiently removes the prefix of the substring that caused the duplication.
2. **Membership Testing**
   Using the `in` operator to check if a character already exists in our current window before deciding whether to expand or shrink.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(N \cdot K)$, where $N$ is the length of the string and $K$ is the length of the current substring. This is because `.index()` and slicing are linear operations. <br>
   **Space Complexity:** $O(min(N, A))$, where $A$ is the size of the character set (alphabet), used to store the current unique substring.