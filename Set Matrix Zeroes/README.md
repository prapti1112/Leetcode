# LeetCode 73: Set Matrix Zeroes

## 📝 Problem Statement
Given an $m \times n$ integer matrix, if an element is 0, set its entire row and column to 0. This must be done **in place**. <br>

**Example 1:** matrix = [[1,1,1],[1,0,1],[1,1,1]] → **Output:** [[1,0,1],[0,0,0],[1,0,1]] <br>

## 🚀 Algorithm: In-Place Marking (First Row/Col as State)
To avoid using $O(m+n)$ extra space, we use the matrix's first row and first column as "flags." We store whether the first row/col themselves need to be zeroed in two variables, then use the rest of the first row/col to mark zeros found in the inner matrix.



**The Logic**
* **Step 1:** Record if the first row or first column originally have a zero.
* **Step 2:** Scan the inner matrix (1,1 to m,n). If `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`.
* **Step 3:** Use those markers to fill the inner matrix with zeros.
* **Step 4:** Use the variables from Step 1 to zero out the first row and column if necessary.

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 2ms (Beats 76.33%)
* **Memory:** 32.30MB (Beats 6.97%)

## 🛠 Programming Paradigm
This follows the **In-Place Modification** paradigm. <br>
* **Resource Re-use:** We treat the first row/column as auxiliary space that we already own.

## 💡 Main Concepts Needed
1. **Contamination Avoidance**
   Separating the "recording" phase from the "writing" phase so that new zeros don't trigger incorrect row/column clears.
2. **Space/Time Complexity** <br>
   **Time Complexity:** $O(m \cdot n)$, traversing the matrix twice. <br>
   **Space Complexity:** $O(1)$, no additional arrays or stacks.