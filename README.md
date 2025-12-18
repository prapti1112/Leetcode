# Leetcode
Implementation for leetcode problem statements

## Day 1 - Maximum Product Subarray

### Riya's Solution

This solution uses dynamic programming with a key insight: unlike the Maximum Subarray Sum problem (Kadane's algorithm) which only tracks the maximum sum, this problem requires tracking both **minimum and maximum products** at each position.

**Why both min and max?** When dealing with products, a negative number can flip the sign. A minimum product (which could be negative) multiplied by a negative number becomes a maximum product. By maintaining both `minp` and `maxp`, the algorithm can handle cases where:
- A negative number multiplied by a negative minimum product yields a positive maximum
- A negative number multiplied by a positive maximum product yields a negative minimum

The algorithm initializes `res` with the maximum element in the array (to handle edge cases), then iterates through the array, updating `maxp` and `minp` at each step by considering three possibilities: the current element alone, current × max product, or current × min product.
