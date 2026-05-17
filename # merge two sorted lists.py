# ============================
# PLATFORM:
# LeetCode (Problem 21 - Merge Two Sorted Lists)
# ============================

# ============================
# PROBLEM:
# You are given two sorted linked lists:
#
#     list1 and list2
#
# Merge them into one sorted linked list
# and return the head of the merged list.
#
# Example:
# Input:
# list1 = [1,2,4]
# list2 = [1,3,4]
#
# Output:
# [1,1,2,3,4,4]
# ============================

# ============================
# APPROACH:
#
# Use ITERATIVE MERGING
#
# Steps:
#
# 1. Create a dummy node.
#
# 2. Use tail pointer
#    to build merged list.
#
# 3. Compare nodes:
#
#    - smaller node is attached
#    - move that list forward
#
# 4. Move tail pointer forward.
#
# 5. After loop:
#    attach remaining nodes.
#
# 6. Return:
#
#       dummy.next
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + m)
#
# n = length of list1
# m = length of list2
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node
        dummy = ListNode()

        # Tail pointer
        tail = dummy

        # Traverse both lists
        while list1 and list2:

            # Choose smaller node
            if list1.val < list2.val:

                tail.next = list1

                list1 = list1.next

            else:

                tail.next = list2

                list2 = list2.next

            # Move tail
            tail = tail.next

        # Attach remaining nodes
        if list1:

            tail.next = list1

        elif list2:

            tail.next = list2

        # Return merged list
        return dummy.next