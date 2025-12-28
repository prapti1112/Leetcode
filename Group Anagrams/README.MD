# LeetCode 49: Group Anagrams

## 📝 Problem Statement
Given an array of strings `strs`, group the **anagrams** together. You can return the answer in any order. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. <br>

**Example 1:** strs = ["eat","tea","tan","ate","nat","bat"] → **Output:** [["bat"],["nat","tan"],["ate","eat","tea"]] <br>
**Example 2:** strs = [""] → **Output:** [[""]] <br>
**Example 3:** strs = ["a"] → **Output:** [["a"]] <br>

## 🚀 Algorithm: Categorize by Sorted String (Hash Map)
The algorithm relies on the fact that all anagrams, when their characters are sorted alphabetically, will result in the exact same string. This "sorted version" serves as a unique key (canonical form) to group the original strings.



**The Logic**
* **Step 1:** **Initialization** — Initialize an empty dictionary `anagrams` to act as our hash map for grouping.
* **Step 2:** **Key Generation** — For each string in the input list, sort its characters and join them back into a string. This `sorted_key` is the unique identifier for that anagram group.
* **Step 3:** **Grouping & Results** — Check if the `sorted_key` exists in the dictionary. If it does, append the original string to that group; if not, create a new list for that key. Finally, return only the values of the dictionary using `list(anagrams.values())`.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 15ms (Beats 49.72%)
* **Memory:** 19.90MB (Beats 99.36%)

## 🛠 Programming Paradigm
This solution follows the **Hash Table / Canonical Form** paradigm. <br>
* **Canonical Form:** By sorting the string, we reduce multiple variations of an anagram to a single, standard representation.
* **Efficient Aggregation:** Using a dictionary allows us to group items in a single pass without the need for nested searches.

## 💡 Main Concepts Needed
1. **String Sorting**
   Sorting converts any anagram into a predictable key. For example, "ate", "eat", and "tea" all become "aet".
2. **Hash Map (Dictionary) Values**
   The dictionary efficiently maps one key to multiple values. Using `list(anagrams.values())` at the end is a clean way to extract the nested groups required by the problem.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(N \cdot K \log K)$, where $N$ is the number of strings and $K$ is the maximum length of a string (due to the sorting of each string). <br>
   **Space Complexity:** $O(N \cdot K)$, required to store the strings in the dictionary.