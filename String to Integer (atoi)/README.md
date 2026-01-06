# LeetCode 8: String to Integer (atoi)

## 📝 Problem Statement
Implement a function `myAtoi(string s)` which converts a string to a 32-bit signed integer. The function must handle leading whitespace, determine the signedness (+ or -), skip leading zeros, stop at the first non-digit character, and clamp the result within the 32-bit signed integer range: $[-2^{31}, 2^{31} - 1]$. <br>

**Example 1:** s = " -042" → **Output:** -42 (Whitespace ignored, sign read, leading zero skipped) <br>
**Example 2:** s = "1337c0d3" → **Output:** 1337 (Reading stops at the first non-digit 'c') <br>
**Example 3:** s = "words and 987" → **Output:** 0 (Reading stops immediately at 'w') <br>

## 🚀 Algorithm: Sequential Rules Processing
This solution follows the problem's requirements step-by-step by cleaning the string, determining the sign, extracting valid digits, and finally performing a mathematical conversion while respecting 32-bit constraints.



**The Logic**
* **Step 1:** **Sanitization** — Use `.strip(" ")` to remove leading/trailing whitespace. Identify the sign by checking the character at index 0 and slice the string to remove the sign and any leading zeros.
* **Step 2:** **Digit Extraction** — Iterate through the remaining characters and collect digits (0-9) using their ASCII values (`ord(c)`). Stop immediately if a non-digit character is encountered.
* **Step 3:** **Conversion & Clamping** — Convert the list of digits into an integer using power-of-10 positional math. Finally, apply the sign and use `min(max(...))` to clamp the value between $-2,147,483,648$ and $2,147,483,647$.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 0ms (Beats 100.00%)
* **Memory:** 17.36MB (Beats 85.30%)

## 🛠 Programming Paradigm
This solution follows the **Procedural / Simulation** paradigm. <br>
* **Step-by-Step Simulation:** The code precisely mimics the logical steps provided in the problem description (Whitespace $\to$ Sign $\to$ Conversion $\to$ Rounding).
* **Early Exit Strategy:** The use of a `break` in the character loop ensures that we don't process invalid trailing data, adhering to the rule that conversion stops at the first non-digit.

## 💡 Main Concepts Needed
1. **ASCII Mapping**
   By using `ord(c) - 48`, we convert the character representation of a digit into its actual integer value without using built-in casting for the whole string.
2. **Positional Notation**
   The formula $n \cdot 10^{length-ind}$ reconstructs the integer by placing each digit in its correct decimal place (units, tens, hundreds, etc.).
3. **Integer Overflow Handling**
   32-bit systems have strict boundaries. Using `2**31` and its negative counterpart allows us to "clamp" any resulting integer that exceeds the physical limits of a 32-bit register.
4. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the string. We traverse the string a constant number of times. <br>
   **Space Complexity:** $O(n)$, specifically to store the `nums` list of digits before conversion.