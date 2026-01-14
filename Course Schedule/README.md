# LeetCode 207: Course Schedule

## 📝 Problem Statement
There are a total of `numCourses` you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses; otherwise, return `false`. <br>

**Example 1:** numCourses = 2, prerequisites = [[1,0]] → **Output:** true (Take course 0, then 1) <br>
**Example 2:** numCourses = 2, prerequisites = [[1,0],[0,1]] → **Output:** false (Circular dependency detected) <br>

## 🚀 Algorithm: Kahn’s Algorithm (Topological Sort via BFS)
This problem is a classic application of cycle detection in a Directed Graph. If the graph is a Directed Acyclic Graph (DAG), we can find a linear ordering of courses; if a cycle exists, it's impossible to finish all courses. Kahn's algorithm works by repeatedly removing nodes with zero "in-degrees" (courses with no remaining prerequisites).



**The Logic**
* **Step 1: Graph Construction** — Build an adjacency list to represent which courses depend on a given prerequisite. Simultaneously, maintain an `in_degree` array to count how many prerequisites each course has.
* **Step 2: Source Identification** — Find all courses with an `in_degree` of `0` and add them to a queue. These are your starting points (courses you can take immediately).
* **Step 3: Process & Decouple** — While the queue isn't empty, "take" a course by popping it. For every course that depends on it, decrement their `in_degree`. If a dependent course's `in_degree` reaches `0`, add it to the queue.
* **Step 4: Cycle Validation** — Keep a counter of how many courses you successfully "took." If the counter equals `numCourses`, the graph is a DAG (True). If not, a cycle exists (False).

## Analysis
* **Difficulty Level:** Medium
* **Runtime:** 3ms (Beats 86.72%)
* **Memory:** 20.36MB (Beats 14.61%)

## 🛠 Programming Paradigm
This solution follows the **Graph Theory / Breadth-First Search (BFS)** paradigm. <br>
* **Degree-Based Filtering:** The core logic relies on tracking the "in-degree" (incoming edges) to determine the processing order.
* **Greedy Processing:** We always take any course that is currently "available" (0 prerequisites), ensuring that we progress through the graph as efficiently as possible.

## 💡 Main Concepts Needed
1. **Directed Acyclic Graph (DAG)**
   A directed graph with no cycles. Topological sorting is only possible on DAGs.
2. **In-Degree Management**
   In a dependency graph, the in-degree represents the number of prerequisites. Reducing the in-degree to zero effectively "unlocks" the next node.
3. **Space/Time Complexity** <br>
   **Time Complexity:** $O(V + E)$, where $V$ is the number of courses and $E$ is the number of prerequisites. We visit every node and every edge exactly once. <br>
   **Space Complexity:** $O(V + E)$, needed to store the adjacency list and the in-degree array.