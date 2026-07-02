# Delete Middle of Linked List

## Platform

GeeksforGeeks

## Problem Link

https://www.geeksforgeeks.org/problems/delete-middle-of-linked-list/1

## Difficulty

Easy

## Topic

- Linked List
- Two Pointers

## Problem Statement

Given the head of a singly linked list, delete the middle node of the linked list and return the head of the modified list.

If the linked list contains only one node, return `NULL`.

## Examples

### Example 1

**Input**

```text
1 → 2 → 3 → 4 → 5
```

**Output**

```text
1 → 2 → 4 → 5
```

**Explanation**

The middle node is `3`, so it is removed from the linked list.

---

### Example 2

**Input**

```text
1 → 2 → 3 → 4
```

**Output**

```text
1 → 2 → 4
```

**Explanation**

For an even-length linked list, the second middle node is deleted.

## Approach

Use the **Slow and Fast Pointer** technique to locate the middle node efficiently.

- Initialize `slow` and `fast` pointers at the head.
- Move `slow` one node at a time and `fast` two nodes at a time.
- Maintain a `prev` pointer to keep track of the node before `slow`.
- When `fast` reaches the end of the list, `slow` points to the middle node.
- Delete the middle node by updating `prev.next` to `slow.next`.
- If the list contains only one node, return `NULL`.

## Algorithm

1. If the list is empty or contains only one node, return `NULL`.
2. Initialize `slow`, `fast`, and `prev`.
3. Traverse the list until `fast` reaches the end.
4. Update `prev.next` to skip the middle node.
5. Return the head of the modified linked list.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concepts

- Slow and Fast Pointer Technique
- Finding the Middle Node
- Linked List Node Deletion

## Solution

The implementation is available in `solution.py`.
