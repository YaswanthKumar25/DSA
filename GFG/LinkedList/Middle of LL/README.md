# Middle of a Linked List

## Platform

GeeksforGeeks

## Problem Link

https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

## Difficulty

Easy

## Topic

* Linked List
* Two Pointers
* Slow and Fast Pointer

## Problem Statement

Given the head of a singly linked list, return the data of the middle node. If the linked list contains an even number of nodes, return the second middle node.

## Example

### Input

```text
1 → 2 → 3 → 4 → 5
```

### Output

```text
3
```

---

### Input

```text
1 → 2 → 3 → 4 → 5 → 6
```

### Output

```text
4
```

## Approach

Use the **Slow and Fast Pointer** technique.

* Initialize two pointers, `slow` and `fast`, at the head.
* Move `slow` one node at a time.
* Move `fast` two nodes at a time.
* When `fast` reaches the end of the linked list, `slow` will be at the middle node.
* Return the data stored in the `slow` node.

## Algorithm

1. Initialize `slow = head` and `fast = head`.
2. Traverse the list while `fast` and `fast.next` are not `None`.
3. Move `slow` by one node.
4. Move `fast` by two nodes.
5. After the loop ends, `slow` points to the middle node.
6. Return `slow.data`.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concepts

* Slow and Fast Pointer Technique
* Two Pointer Approach
* Linked List Traversal

## Solution

The implementation is available in `solution.py`.
