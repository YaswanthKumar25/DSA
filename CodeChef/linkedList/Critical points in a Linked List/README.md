# Critical Points in a Linked List

## Platform

CodeChef

## Problem Link

https://www.codechef.com/practice/course/linked-lists/LINKLISTF/problems/CRITLIST

## Difficulty

Medium

## Topic

* Linked List
* Traversal
* Pointer Manipulation

## Problem Statement

Given the head of a singly linked list, determine the number of **critical points** in the list.

A node is considered a **critical point** if:

* It is a **local maximum**, i.e., its value is strictly greater than both its previous and next nodes.
* It is a **local minimum**, i.e., its value is strictly smaller than both its previous and next nodes.

The first and last nodes cannot be critical points because they do not have both a previous and a next node.

## Example

### Input

```text
1 → 3 → 2 → 4 → 1 → 5
```

### Output

```text
4
```

### Explanation

The critical points are:

* `3` (local maximum)
* `2` (local minimum)
* `4` (local maximum)
* `1` (local minimum)

## Approach

Traverse the linked list while maintaining three consecutive nodes:

* `prev`
* `curr`
* `next`

For each middle node (`curr`):

* If `curr.val > prev.val` and `curr.val > next.val`, it is a local maximum.
* If `curr.val < prev.val` and `curr.val < next.val`, it is a local minimum.

Increment the count whenever either condition is satisfied.

## Algorithm

1. If the linked list contains fewer than three nodes, return `0`.
2. Initialize `prev` as the head and `curr` as the second node.
3. Traverse the linked list while `curr.next` exists.
4. Check whether the current node is a local maximum or local minimum.
5. Increment the counter if it is a critical point.
6. Move all pointers one step forward.
7. Return the total number of critical points.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concepts

* Linked List Traversal
* Local Maximum
* Local Minimum
* Pointer Manipulation
* Single Pass Algorithm

## Solution

The implementation is available in `solution.py`.
