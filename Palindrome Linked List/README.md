# LeetCode 234: Palindrome Linked List

## 📝 Problem Statement
Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise. A linked list is a palindrome if the sequence of values is the same when read forwards and backwards. <br>

**Example 1:** head = [1,2,2,1] → **Output:** true ([1,2,2,1] reads the same both ways) <br>
**Example 2:** head = [1,2] → **Output:** false ([1,2] read backwards is [2,1]) <br>

## 🚀 Algorithm: Array Conversion & Reverse Slicing
Because a singly linked list can only be traversed in one direction, this approach converts the list nodes into a Python list (array). This "flattens" the data structure, allowing us to use Python's highly optimized internal slicing and comparison methods to check for symmetry.



**The Logic**
* **Step 1:** **Initialization** — Create an empty list `vals` and a pointer `current` initialized to the `head` of the linked list.
* **Step 2:** **Linear Traversal** — Traverse the linked list using a `while` loop. In each iteration, append the current node's value to `vals` and move to the next node.
* **Step 3:** **Symmetry Comparison** — Use Python's slicing syntax `vals[::-1]` to create a reversed version of the array and compare it to the original. Return `true` if they match, `false` otherwise.

## Analysis
* **Difficulty Level:** Easy
* **Runtime:** 13ms (Beats 96.23%)
* **Memory:** 53.68MB (Beats 5.18%)

## 🛠 Programming Paradigm
This solution follows the **Data Transformation** paradigm. <br>
* **Structural Simplification:** We transform a complex, non-indexed structure (Linked List) into a simple, indexed structure (Array) to solve the problem more easily.
* **Space-Time Tradeoff:** We sacrifice memory (storing the values) to achieve a very fast and readable solution using built-in language features.

## 💡 Main Concepts Needed
1. **Linked List Traversal**
   The ability to navigate a singly linked list by following the `.next` pointers until reaching a `null` value.
2. **Python List Slicing**
   Understanding how `[::-1]` works to efficiently reverse a sequence for comparison.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. We visit each node exactly once to build the array and then perform a linear comparison. <br>
   **Space Complexity:** $O(n)$, as we create a new array to store all values from the linked list.