# LeetCode 811: Subdomain Visit Count

## 📝 Problem Statement
A website domain like "discuss.leetcode.com" consists of various subdomains (e.g., "leetcode.com" and "com"). Given an array of count-paired domains `cpdomains` (like "9001 discuss.leetcode.com"), return an array of count-paired domains representing the aggregated visits for each subdomain. <br>

**Example 1:** cpdomains = ["9001 discuss.leetcode.com"] → **Output:** ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"] (All levels inherit the visit count) <br>
**Example 2:** cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"] → **Output:** ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"] (Aggregated counts for shared subdomains like "com" and "mail.com") <br>

## 🚀 Algorithm: Hash Map Aggregation
The approach uses a Hash Map (Dictionary) to aggregate visit counts for every possible subdomain encountered. By processing each entry and splitting it into all valid suffixes, we can sum the counts efficiently in a single pass.



**The Logic**
* **Step 1:** **Initialization** — Create an empty dictionary `frequencies` to store the mapping of `subdomain -> total_count`.
* **Step 2:** **Decomposition & Accumulation** — Iterate through each input string. Split the count and the domain. Then, split the domain by `.` to get individual parts. Iterate through these parts to reconstruct every possible subdomain (suffix) and add the current count to that subdomain's entry in `frequencies`.
* **Step 3:** **Formatting** — Convert the key-value pairs from the dictionary back into the string format `"count domain"` and return the list.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 3ms (Beats 91.80%)
* **Memory:** 17.36MB (Beats 95.82%)

## 🛠 Programming Paradigm
This solution follows the **Hash Table / Frequency Counting** paradigm. <br>
* **Key-Value Mapping:** We utilize the dictionary to handle the "many-to-one" relationship where multiple full domains (e.g., "google.mail.com", "intel.mail.com") contribute to the same subdomain ("mail.com").
* **String Manipulation:** The logic heavily relies on splitting strings to isolate components and joining them back together to form valid keys.

## 💡 Main Concepts Needed
1. **String Parsing (Split & Join)**
   Essential for separating the integer count from the domain string, and then breaking the domain into hierarchical levels (e.g., "a.b.c" $\to$ ["a", "b", "c"]).
2. **Hash Maps (Dictionaries)**
   Used to store unique subdomains and accumulate their visit counts efficiently without needing to search through a list repeatedly.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(N \cdot L)$, where $N$ is the number of domains and $L$ is the length of the domain strings. We process every character and subdomain suffix once. <br>
   **Space Complexity:** $O(N \cdot L)$, as we must store every unique subdomain and its count in the dictionary.