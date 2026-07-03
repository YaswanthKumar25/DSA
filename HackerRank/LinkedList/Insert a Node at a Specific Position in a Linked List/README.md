# Insert a Node at a Specific Position in a Linked List

## Platform

HackerRank

## Problem Link

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

## Difficulty

Easy

## Topic

* Linked List
* Pointer Manipulation

## Problem Statement

Given the head of a singly linked list, an integer `data`, and a zero-based `position`, insert a new node containing `data` at the specified position and return the head of the updated linked list.

## Example

### Input

```text
Linked List: 16 → 13 → 7
Data: 1
Position: 2
```

### Output

```text
16 → 13 → 1 → 7
```

## Approach

* Create a new node containing the given `data`.
* If `position == 0`, insert the node at the beginning of the list and return the new head.
* Otherwise, traverse the linked list until reaching the node just before the desired position.
* Update the pointers so that the new node is inserted without losing the remaining part of the list.

## Algorithm

1. Create a new node.
2. If `position == 0`:

   * Set `new_node.next = head`.
   * Return `new_node`.
3. Traverse to the node at index `position - 1`.
4. Store the next node.
5. Link the current node to the new node.
6. Link the new node to the stored next node.
7. Return the head.

## Edge Cases

* Insert at the beginning (`position = 0`).
* Insert at the end of the linked list.
* Insert in the middle of the linked list.
* List contains only one node.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concepts

* Singly Linked List
* Node Insertion
* Pointer Manipulation
* Edge Case Handling

## Solution

The implementation is available in `solution.py`.
