# LeetCode 225: Implement Stack using Queues

## 📝 Problem Statement
Implement a Last-In-First-Out (LIFO) stack using only standard queue operations (`push to back`, `peek/pop from front`, `size`, and `is empty`). <br>

**Example:**
* Push(1), Push(2)
* Top() → 2
* Pop() → 2
* Empty() → false

## 🚀 Algorithm: Single Queue Rotation
While the problem allows for two queues, a more elegant and space-efficient approach uses a single queue. By rotating the queue every time a new element is added, we force the queue to behave like a stack where the most recently added element is always at the "exit" (the front).



**The Logic**
* **Step 1: Push & Append** — Add the new element `x` to the back of the queue.
* **Step 2: Re-order** — Calculate the current size of the queue. Loop `size - 1` times: remove the front element and immediately add it back to the rear.
* **Step 3: Access** — Because of the rotation in Step 2, the `pop` and `top` operations simply look at the front of the queue, resulting in $O(1)$ performance.

## Analysis
* **Difficulty Level:** Easy
* **Runtime:** 0ms (Beats 100%)
* **Memory:** 19.84MB (Beats 9.16%)

## 🛠 Programming Paradigm
This solution follows the **Adapter Pattern / Structural Simulation** paradigm. <br>
* **Interface Transformation:** We are wrapping one data structure's interface (FIFO) to mimic another (LIFO).
* **Work-Heavy Ingestion:** We shift the complexity to the `push` operation to ensure all other operations remain "lazy" and fast.

## 💡 Main Concepts Needed
1. **FIFO vs. LIFO**
   Understanding that a Queue processes the "oldest" data first, while a Stack processes the "newest" data first.
2. **Queue Rotation**
   The technique of moving elements from the front to the back to change their relative order.
3. **Space/Time Complexity** <br>
   **Time Complexity:** - `push`: $O(n)$, where $n$ is the number of elements.
   - `pop/top/empty`: $O(1)$. <br>
   **Space Complexity:** $O(n)$, to store the elements in the queue.