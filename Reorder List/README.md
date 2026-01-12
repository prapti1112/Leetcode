# LeetCode 143: Reorder List

## 📝 Problem Statement
Given the head of a singly linked list, reorder the list to follow the specific pattern: $L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow L_2 \rightarrow L_{n-2} \rightarrow \dots$. You must modify the nodes in-place without changing their values. <br>

**Example 1:** [1,2,3,4] → **Output:** [1,4,2,3] (The last node '4' is moved after '1') <br>
**Example 2:** [1,2,3,4,5] → **Output:** [1,5,2,4,3] (Nodes are 'weaved' from both ends inward) <br>

## 🚀 Algorithm: Three-Phase In-Place Manipulation
This approach was chosen to achieve optimal time and space complexity. Since we cannot easily access the end of a singly linked list, we break the problem into three logical sub-tasks: finding the midpoint, reversing the latter half to allow "backward" traversal, and interleaving the two resulting halves.



**The Logic**
* **Step 1: Finding the Middle** — Utilize the **Slow and Fast Pointer** (Tortoise and Hare) technique to identify the center of the list.
* **Step 2: Reversing the Tail** — Cut the list at the midpoint and reverse the second half in-place. This provides a pointer to the end of the original list ($L_n$) that can now move toward the middle.
* **Step 3: Interleaving (Merging)** — Using two pointers (one at the start of the first half and one at the start of the reversed second half), weave the nodes together by updating their `.next` references.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 1ms (Beats 59.31%)
* **Memory:** 28.11MB (Beats 6.70%)

## 🛠 Programming Paradigm
This solution follows the **In-Place Linked List Manipulation** paradigm. <br>
* **Pointer Redirection:** Instead of creating new data structures (like a stack or array), we modify the existing `next` pointers of the nodes.
* **Structural Decomposition:** The complex reordering is simplified by decomposing it into standard linked list operations (Find Middle + Reverse + Merge).

## 💡 Main Concepts Needed
1. **Slow and Fast Pointers**
   Crucial for finding the midpoint of a singly linked list in $O(n)$ time without knowing the list's total length beforehand.
2. **Iterative List Reversal**
   A fundamental technique to reverse the direction of a linked list by tracking `prev`, `curr`, and `next` nodes.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(n)$, where $n$ is the number of nodes. We traverse the list to find the middle, traverse the second half to reverse it, and traverse again to merge. <br>
   **Space Complexity:** $O(1)$, as we only use a constant amount of extra space for pointers regardless of list size.