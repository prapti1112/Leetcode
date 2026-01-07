# LeetCode 151: Reverse Words in a String

## 📝 Problem Statement
Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. The output should be a single string with words in reverse order, joined by a single space, with no leading or trailing spaces. <br>

**Example 1:** s = "the sky is blue" → **Output:** "blue is sky the" <br>
**Example 2:** s = "  hello world  " → **Output:** "world hello" (Leading/trailing spaces removed) <br>
**Example 3:** s = "a good   example" → **Output:** "example good a" (Multiple spaces reduced to one) <br>

## 🚀 Algorithm: Tokenization and List Reversal
The algorithm leverages Python's high-level string methods to clean and split the input into a list of words (tokens). By filtering out empty strings and reversing the resulting list, we can easily reconstruct the string in the desired order.



**The Logic**
* **Step 1:** **Cleaning and Splitting** — Use `.strip()` to remove surrounding whitespace and `.split(" ")` to break the string into a raw list of potential words.
* **Step 2:** **Filtering and Reversing** — Use a list comprehension to keep only valid "non-space" characters, ensuring multiple internal spaces are ignored. Then, reverse this filtered list using the slicing operator `[::-1]`.
* **Step 3:** **Re-joining** — Use the `" ".join()` method to concatenate the reversed words into a single string with a single space as the separator.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 0ms (Beats 100.00%)
* **Memory:** 19.54MB (Beats 15.79%)

## 🛠 Programming Paradigm
This solution follows the **Functional / String Processing** paradigm. <br>
* **Data Transformation Pipeline:** The logic treats the input as a stream of data that passes through a series of transformations: Strip $\rightarrow$ Split $\rightarrow$ Filter $\rightarrow$ Reverse $\rightarrow$ Join.
* **Declarative Approach:** Instead of managing manual pointers and indices, the solution uses Python's built-in optimized C-functions to handle memory and string reconstruction.

## 💡 Main Concepts Needed
1. **Tokenization**
   Breaking a continuous string into discrete "words" based on a delimiter (space). Python's `split()` is highly optimized for this.
2. **List Comprehension**
   A concise way to filter data. In this case, it ensures that only actual words make it into the final list, effectively handling the "multiple spaces" constraint.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the length of the string. We traverse the string to split, filter, reverse, and join, all of which are linear operations. <br>
   **Space Complexity:** $O(n)$, as we create an intermediate list of words that stores the characters of the original string.