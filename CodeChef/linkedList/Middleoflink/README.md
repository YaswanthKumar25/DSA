# Middle of the Linked List

## Platform

LeetCode

## Problem Link

https://leetcode.com/problems/middle-of-the-linked-list/

## Difficulty

Easy

## Topic

- Linked List
- Two Pointers

## Problem Statement

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

## Approach

Use two pointers:

- **Slow Pointer:** Moves one node at a time.
- **Fast Pointer:** Moves two nodes at a time.

Since the fast pointer travels twice as fast as the slow pointer, when the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

If the linked list has an even number of nodes, this approach naturally returns the second middle node.

## Algorithm

1. If the list is empty or contains only one node, return the head.
2. Initialize two pointers, `slow` and `fast`, at the head.
3. While `fast` and `fast.next` are not `None`:
   - Move `slow` one step forward.
   - Move `fast` two steps forward.

4. Return the `slow` pointer.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Key Concept

The Slow and Fast Pointer technique is widely used in linked list problems such as:

- Finding the middle node
- Detecting a cycle
- Finding the start of a cycle
- Checking if a linked list is a palindrome
- Splitting a linked list

## Solution

Implemented in `solution.py`.
