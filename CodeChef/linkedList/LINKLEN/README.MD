# Length of Linked List (LINKLEN)

## Problem Link

https://www.codechef.com/practice/course/linked-lists/LINKLISTF/problems/LINKLEN

## Platform

CodeChef

## Topic

Linked List

## Difficulty

Easy

## Problem Statement

Given the head of a singly linked list, return the number of nodes present in the linked list.

## Approach

Start from the head node and traverse the linked list one node at a time. Maintain a counter that is incremented for every visited node. Continue until the current node becomes `None`. The final value of the counter is the length of the linked list.

## Algorithm

1. Initialize a counter `cnt` to `0`.
2. Set the current node to `head`.
3. While the current node is not `None`:

   * Increment `cnt` by `1`.
   * Move to the next node.
4. Return `cnt`.

## Time Complexity

**O(n)**, where `n` is the number of nodes in the linked list.

## Space Complexity

**O(1)**

## Solution File

`Length_of_Linked_List.py`
