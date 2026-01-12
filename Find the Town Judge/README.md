# LeetCode 997: Find the Town Judge

## 📝 Problem Statement
In a town of `n` people, a town judge exists if they trust nobody and are trusted by everyone else. Given a `trust` array of pairs `[a, b]`, identify the judge. <br>

**Example 1:** n = 2, trust = [[1,2]] → **Output:** 2 (Person 2 is trusted by 1 and trusts no one) <br>
**Example 2:** n = 3, trust = [[1,2],[2,3]] → **Output:** -1 (No one is trusted by everyone else) <br>

## 🚀 Algorithm: Degree Counting (Indegree - Outdegree)
This approach treats the problem as a directed graph. The judge is the only node with an "in-degree" of $n-1$ and an "out-degree" of $0$. By maintaining a single array to track the net score ($in - out$), we can find the judge in a single pass.



**The Logic**
* **Step 1: Score Tracking** — Initialize an array `trust_scores` of size $n+1$ with zeros.
* **Step 2: Balance Updates** — Iterate through the `trust` list. For every `[a, b]`, decrement the score of person `a` (the truster) and increment the score of person `b` (the trustee).
* **Step 3: Identification** — Loop through the scores from $1$ to $n$. If any person has a score equal to $n-1$, return that person as the judge. Otherwise, return $-1$.

## Analysis
* **Difficulty Level:** Easy
* **Runtime:** 15ms (57.23%)
* **Memory:** 22.63MB (5.89%)

## 🛠 Programming Paradigm
This solution follows the **Graph Theory / Frequency Counting** paradigm. <br>
* **Graph Modeling:** Representing relationships as edges between nodes allows us to use degree properties to find a specific node.
* **Space-Efficient Mapping:** Instead of a full adjacency list, a single frequency array captures all necessary state.

## 💡 Main Concepts Needed
1. **In-Degree vs. Out-Degree**
   Essential for identifying the "sink" of a directed graph (a node where all edges point in, and none point out).
2. **Net Change Aggregation**
   Combining two properties into one score ($+1$ for being trusted, $-1$ for trusting) simplifies the final check into one comparison.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(T + n)$, where $T$ is the number of trust relationships. We iterate through the trust list once and the people once. <br>
   **Space Complexity:** $O(n)$, required to store the trust scores for each of the $n$ people.