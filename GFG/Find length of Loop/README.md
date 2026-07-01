# Find Length of Loop in a Linked List

## Platform

GeeksforGeeks

## Problem Link

https://www.geeksforgeeks.org/problems/find-length-of-loop/1

## Difficulty

Medium

## Topic

- Linked List
- Floyd's Cycle Detection
- Two Pointers

## Problem Statement

Given the head of a singly linked list, determine whether the list contains a loop. If a loop exists, return the number of nodes present in the loop. Otherwise, return `0`.

## Examples

### Example 1

**Input**

```text
1 → 2 → 3 → 4 → 5
     ↑         ↓
     └─────────┘
```

**Output**

```text
4
```

### Example 2

**Input**

```text
1 → 2 → 3 → 4 → NULL
```

**Output**

```text
0
```

## Approach

The solution uses **Floyd's Cycle Detection Algorithm (Slow and Fast Pointer)**.

- Initialize two pointers:
  - `slow` moves one node at a time.
  - `fast` moves two nodes at a time.

- If the pointers meet, a loop exists.
- Keep one pointer fixed and move the other pointer around the loop until it reaches the fixed pointer again.
- Count the number of steps taken during this traversal. This count is the length of the loop.

## Algorithm

1. Initialize `slow` and `fast` to the head.
2. Move `slow` by one step and `fast` by two steps.
3. If they meet, a cycle is detected.
4. Traverse the cycle once to count its length.
5. Return the count.
6. If no cycle is found, return `0`.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concepts

- Floyd's Cycle Detection Algorithm
- Slow and Fast Pointer Technique
- Cycle Length Calculation

## Solution

The implementation is available in `solution.py`.
